"""Read public source metadata without paid services."""

from __future__ import annotations

import html
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import UTC, datetime
from typing import Any

USER_AGENT = "trading-engine-research/0.1 (local strategy research)"
QUERY_ALIASES = {
    "orb": "open range breakout trading strategy",
    "open range breakout": "open range breakout trading strategy",
}
CRYPTO_WORDS = ("crypto", "cryptocurrency", "bitcoin", "ethereum", "binance", "token", "digital asset")
MARKET_WORDS = {
    "crypto": CRYPTO_WORDS,
    "stocks": ("stock", "equity", "shares", "s&p 500", "yfinance", "nasdaq", "nyse", "market open"),
    "futures": ("futures", "perpetual", "perp"),
    "forex": ("forex", "foreign exchange", "currency pair", " fx "),
}
FINANCE_WORDS = ("trading", "trade", "backtest", "investment", "portfolio", "market", "finance", "financial", "exchange")


def expand_query(query: str) -> str:
    """Turn common trading shortcuts into clear search words."""
    return QUERY_ALIASES.get(" ".join(query.lower().split()), query)


def classify_market(record: dict[str, Any]) -> str:
    """Find the main market named by the source."""
    text = f"{record.get('title', '')} {record.get('summary', '')}".lower()
    for market in ("futures", "crypto", "forex", "stocks"):
        if any(word in text for word in MARKET_WORDS[market]):
            return market
    return "other"


def is_strategy_source(record: dict[str, Any], query: str) -> bool:
    """Reject unrelated pages that happen to contain a short strategy name."""
    text = f"{record.get('title', '')} {record.get('summary', '')}".lower()
    if not any(word in text for word in FINANCE_WORDS):
        return False
    if "open range breakout" in query.lower():
        return any(phrase in text for phrase in ("open range", "opening range", "breakout"))
    keywords = [word for word in re.findall(r"[a-z0-9]+", query.lower()) if word not in {"trading", "strategy", "strategies", "market"}]
    return not keywords or any(word in text for word in keywords)


def fetch_json(url: str) -> dict[str, Any]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def fetch_text(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", value)
    return " ".join(html.unescape(value).split())


def search_arxiv(query: str, limit: int) -> list[dict[str, Any]]:
    # arXiv treats a plain multi-word query loosely. Require every word instead.
    words = re.findall(r"[a-zA-Z0-9]+", query)
    search_query = " AND ".join(f"all:{word}" for word in words)
    params = urllib.parse.urlencode(
        {"search_query": search_query, "start": 0, "max_results": limit}
    )
    root = ET.fromstring(fetch_text(f"https://export.arxiv.org/api/query?{params}"))
    atom = "{http://www.w3.org/2005/Atom}"
    records = []
    for entry in root.findall(f"{atom}entry"):
        link = entry.findtext(f"{atom}id", default="")
        records.append(
            {
                "source": "arxiv",
                "id": link.rsplit("/", 1)[-1],
                "title": clean_text(entry.findtext(f"{atom}title")),
                "url": link,
                "published": entry.findtext(f"{atom}published", default=""),
                "authors": [
                    clean_text(author.findtext(f"{atom}name"))
                    for author in entry.findall(f"{atom}author")
                ],
                "summary": clean_text(entry.findtext(f"{atom}summary")),
                "license": "Check the source page before reuse.",
            }
        )
    return records


def search_crossref(query: str, limit: int) -> list[dict[str, Any]]:
    params = urllib.parse.urlencode({"query": query, "rows": limit})
    payload = fetch_json(f"https://api.crossref.org/works?{params}")
    records = []
    for item in payload["message"]["items"]:
        licenses = [license_item.get("URL", "") for license_item in item.get("license", [])]
        records.append(
            {
                "source": "crossref",
                "id": item.get("DOI", ""),
                "title": clean_text((item.get("title") or [""])[0]),
                "url": item.get("URL", ""),
                "published": "-".join(
                    str(part)
                    for part in (item.get("published", {}).get("date-parts", [[""]])[0])
                ),
                "authors": [
                    " ".join(filter(None, [author.get("given"), author.get("family")]))
                    for author in item.get("author", [])
                ],
                "summary": clean_text(item.get("abstract")),
                "license": ", ".join(licenses) if licenses else "Check the source page before reuse.",
            }
        )
    return records


def search_github(query: str, limit: int) -> list[dict[str, Any]]:
    params = urllib.parse.urlencode({"q": query, "per_page": limit})
    payload = fetch_json(f"https://api.github.com/search/repositories?{params}")
    records = []
    for item in payload["items"]:
        license_data = item.get("license") or {}
        records.append(
            {
                "source": "github",
                "id": item["full_name"],
                "title": item["full_name"],
                "url": item["html_url"],
                "published": item.get("updated_at", ""),
                "authors": [item.get("owner", {}).get("login", "")],
                "summary": clean_text(item.get("description")),
                "license": license_data.get("spdx_id") or "Check the repository before reuse.",
            }
        )
    return records


COLLECTORS = {
    "arxiv": search_arxiv,
    "crossref": search_crossref,
    "github": search_github,
}


def search(source: str, query: str, limit: int) -> list[dict[str, Any]]:
    if source not in COLLECTORS:
        raise ValueError(f"Unknown source: {source}")
    return COLLECTORS[source](query, limit)


def new_result_file(query: str, source: str) -> str:
    safe_query = re.sub(r"[^a-z0-9]+", "-", query.lower()).strip("-")[:50] or "search"
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    return f"{timestamp}_{source}_{safe_query}.json"
