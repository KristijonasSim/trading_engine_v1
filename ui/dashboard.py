"""Read local project files for the dashboard."""

from __future__ import annotations

import json
import re
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from research_engine.collectors import classify_market


def deleted_sources_path(project_root: Path) -> Path:
    return project_root / "data" / "research" / "deleted_sources.json"


def read_deleted_sources(project_root: Path) -> set[tuple[str, str]]:
    path = deleted_sources_path(project_root)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return set()
    return {
        (item["source"], item["id"])
        for item in payload.get("deleted", [])
        if item.get("source") and item.get("id")
    }


def delete_source(project_root: Path, source: str, record_id: str) -> None:
    path = deleted_sources_path(project_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    deleted = read_deleted_sources(project_root)
    deleted.add((source, record_id))
    payload = {
        "deleted": [
            {"source": item_source, "id": item_id, "deleted_at": datetime.now(UTC).isoformat()}
            for item_source, item_id in sorted(deleted)
        ]
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def read_records(project_root: Path) -> list[dict[str, Any]]:
    records_by_key: dict[tuple[str, str], dict[str, Any]] = {}
    deleted = read_deleted_sources(project_root)
    for path in sorted((project_root / "data" / "research").glob("*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        harvested_at = payload.get("created_at")
        if not harvested_at:
            harvested_at = datetime.fromtimestamp(path.stat().st_mtime, UTC).isoformat()
        for position, record in enumerate(payload.get("records", [])):
            if not record.get("source") or not record.get("id"):
                continue
            if (record["source"], record["id"]) in deleted:
                continue
            saved_record = {
                **record,
                "harvested_at": harvested_at,
                "_sort_key": (harvested_at, -position),
            }
            records_by_key[(record["source"], record["id"])] = saved_record
    return sorted(records_by_key.values(), key=lambda item: item["_sort_key"], reverse=True)


def display_title(record: dict[str, Any]) -> str:
    """Make a short title while keeping the main strategy idea."""
    text = f"{record.get('title', '')} {record.get('summary', '')}".lower()
    if record.get("source") == "github":
        owner = record.get("id", "source").split("/", 1)[0]
        if "momentum" in text:
            return f"{owner} Momentum"
        if "mean reversion" in text:
            return f"{owner} Mean Reversion"
        if "trend" in text:
            return f"{owner} Trend"
        return owner
    if "time-series momentum" in text:
        return "Risk-Managed Crypto Momentum" if "risk-managed" in text else "Crypto Time-Series Momentum"
    if "trend-following" in text:
        return "Adaptive Crypto Trend-Following" if "adaptive" in text else "Crypto Trend-Following"
    if "momentum" in text:
        return "Crypto Momentum Strategy"
    return record.get("title") or record.get("id") or "Untitled source"


def market_type(record: dict[str, Any]) -> str:
    return classify_market(record)


def read_cards(project_root: Path) -> list[dict[str, str]]:
    cards = []
    for path in sorted((project_root / "strategy_cards").glob("*.md")):
        try:
            content = path.read_text(encoding="utf-8")
        except OSError:
            continue
        title_match = re.search(r"^# Strategy card: (.+)$", content, re.MULTILINE)
        status_match = re.search(r"^- Status: `([^`]+)`", content, re.MULTILINE)
        decision_match = re.search(r"^- Decision: `?([^`\n]+)`?", content, re.MULTILINE)
        cards.append(
            {
                "file": path.name,
                "title": title_match.group(1) if title_match else path.stem,
                "status": status_match.group(1) if status_match else "unknown",
                "decision": decision_match.group(1).strip() if decision_match else "needs review",
            }
        )
    return cards


def dashboard_data(project_root: Path) -> dict[str, Any]:
    records = read_records(project_root)
    for record in records:
        record["short_title"] = display_title(record)
        record["market"] = market_type(record)
    cards = read_cards(project_root)
    source_counts = Counter(record["source"] for record in records)
    testing_reports = list((project_root / "data" / "testing").glob("*.json"))
    return {
        "research": {
            "state": "ready",
            "unique_sources": len(records),
            "source_counts": dict(sorted(source_counts.items())),
            "records": records[:25],
        },
        "testing": {
            "state": "not built",
            "strategy_cards": len(cards),
            "reports": len(testing_reports),
        },
        "bot": {
            "state": "not built",
            "live_strategies": 0,
            "open_positions": 0,
        },
        "strategy_cards": cards,
    }
