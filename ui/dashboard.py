"""Read local project files for the dashboard."""

from __future__ import annotations

import json
import re
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from research_engine.collectors import classify_market
from strategy_adapter.adapters import write_adapter
from strategy_adapter.queue import load as load_queue
from testing_engine.policy import MIN_PROFIT_FACTOR, MIN_TRADES_PER_DAY, candidate_timeframes, public_policy


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
    is_crypto_market = classify_market(record) in {"crypto", "futures"}
    if record.get("source") == "github":
        owner = record.get("id", "source").split("/", 1)[0]
        if "momentum" in text:
            return f"{owner} Momentum"
        if "mean reversion" in text:
            return f"{owner} Mean Reversion"
        if "trend" in text:
            return f"{owner} Trend"
        return owner
    if "time-series momentum" in text and is_crypto_market:
        return "Risk-Managed Crypto Momentum" if "risk-managed" in text else "Crypto Time-Series Momentum"
    if "trend-following" in text and is_crypto_market:
        return "Adaptive Crypto Trend-Following" if "adaptive" in text else "Crypto Trend-Following"
    if "momentum" in text and is_crypto_market:
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


def read_adapters(project_root: Path) -> list[dict[str, str]]:
    adapters = []
    for path in sorted((project_root / "strategy_adapters").glob("*.md")):
        content = path.read_text(encoding="utf-8")
        title = re.search(r"^# Strategy adapter: (.+)$", content, re.MULTILINE)
        target = re.search(r"^- Target: `([^`]+)`", content, re.MULTILINE)
        status = re.search(r"^- Status: `([^`]+)`", content, re.MULTILINE)
        source = re.search(r"^- Link: (.+)$", content, re.MULTILINE)
        market = re.search(r"^- Source market: `([^`]+)`", content, re.MULTILINE)
        note = re.search(r"^- Result: (.+)$", content, re.MULTILINE)
        adapters.append({"file": path.name, "title": title.group(1) if title else path.stem, "target": target.group(1) if target else "unknown", "status": status.group(1) if status else "draft", "source_link": source.group(1) if source else "", "source_market": market.group(1) if market else "unknown", "note": note.group(1) if note else ""})
    return adapters


def read_testing_strategies(project_root: Path, reports: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Only code that can be tested belongs in the test queue."""
    latest_reports: dict[tuple[str, str], dict[str, Any]] = {}
    for report in sorted(reports, key=lambda item: item.get("created_at", "")):
        if report.get("strategy"):
            key = (str(report["strategy"]), str(report.get("timeframe") or ""))
            latest_reports[key] = report
    try:
        registry = json.loads((project_root / "testing_engine" / "registry.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        registry = {}
    runnable = []
    for file in sorted((project_root / "testing_engine" / "strategies").glob("*.py")):
        if file.name == "__init__.py":
            continue
        try:
            config = json.loads((project_root / "testing_engine" / "configs" / f"{file.stem}.json").read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            config = {}
        if registry.get(file.stem, {}).get("duplicate_of"):
            continue
        suggested_timeframe = config.get("timeframe", "1h")
        comparison_timeframes = candidate_timeframes(suggested_timeframe)
        legacy_report = latest_reports.get((file.stem, ""), {})
        timeframe_reports = {
            timeframe: latest_reports.get(
                (file.stem, timeframe),
                legacy_report if timeframe == suggested_timeframe else {},
            )
            for timeframe in comparison_timeframes
        }
        terminal = {"baseline_passed", "baseline_failed", "rejected", "nautilus_queue"}
        completed = [report for report in timeframe_reports.values() if report.get("status") in terminal]
        passed = [report for report in completed if report.get("status") == "baseline_passed" and report.get("metrics")]
        def rank(report: dict[str, Any]) -> float:
            try:
                return float(report.get("metrics", {}).get("score", "-1"))
            except (TypeError, ValueError):
                return -1
        def meets_goal(report: dict[str, Any]) -> bool:
            try:
                metrics = report.get("metrics", {})
                return float(str(metrics.get("pf", "0")).replace("%", "")) > MIN_PROFIT_FACTOR and float(str(metrics.get("trades_per_day", "0")).replace("%", "")) >= MIN_TRADES_PER_DAY
            except (TypeError, ValueError):
                return False
        qualifying = [report for report in passed if meets_goal(report)]
        best = max(qualifying or passed or completed or list(timeframe_reports.values()), key=rank, default={})
        if len(completed) == len(comparison_timeframes):
            status = "passed_goal" if qualifying else "failed_goal"
        elif any(report.get("status") == "running" for report in timeframe_reports.values()):
            status = "running"
        else:
            status = "ready_for_comparison"
        runnable.append({
            "name": registry.get(file.stem, {}).get("source_title", file.stem),
            "code_name": file.stem,
            "kind": "AI hypothesis" if registry.get(file.stem, {}).get("hypothesis") else "Source rules",
            "timeframe": best.get("timeframe") or suggested_timeframe,
            "comparison_timeframes": list(comparison_timeframes),
            "completed_timeframes": len(completed),
            "status": status,
            "qualifies": bool(qualifying),
            "metrics": best.get("metrics", {}),
            "timerange": report.get("timerange", public_policy()["timerange"]),
        })
    return runnable


def create_adapter(project_root: Path, source: str, record_id: str, target: str) -> Path | None:
    record = next((item for item in read_records(project_root) if item["source"] == source and item["id"] == record_id), None)
    if record is None:
        return None
    record["short_title"] = display_title(record)
    record["market"] = market_type(record)
    return write_adapter(record, target, project_root / "strategy_adapters")


def dashboard_data(project_root: Path) -> dict[str, Any]:
    records = read_records(project_root)
    for record in records:
        record["short_title"] = display_title(record)
        record["market"] = market_type(record)
    cards = read_cards(project_root)
    adapters = read_adapters(project_root)
    pending_adapters = [item for item in adapters if item["status"] not in {"adapted", "ai_hypothesis", "duplicate_hypothesis"}]
    archived_adapters = [item for item in adapters if item["status"] == "duplicate_hypothesis"]
    source_states = {item["source_link"]: item["status"] for item in adapters if item["source_link"]}

    # Keep the Research inbox useful: fresh, actionable market ideas first.
    # Stock, forex and futures logic can be translated into BTC hypotheses;
    # only genuinely non-market material stays below the active inbox.
    completed_states = {"adapted", "ai_hypothesis", "duplicate_hypothesis"}
    records.sort(key=lambda item: item["_sort_key"], reverse=True)
    records.sort(
        key=lambda item: 0
        if item["market"] in {"crypto", "futures", "stocks", "forex", "general"}
        and source_states.get(item.get("url", "")) not in completed_states
        else 1
    )
    queue = load_queue(project_root)
    source_counts = Counter(record["source"] for record in records)
    # Import here to keep the dashboard's portable-history behavior exactly the
    # same as the autonomous worker's skip logic.
    from testing_engine.__main__ import read_shared_history
    testing_reports = read_shared_history(project_root)
    jobs = []
    for path in (project_root / "data" / "testing" / "jobs").glob("*.json"):
        try:
            jobs.append(json.loads(path.read_text(encoding="utf-8")))
        except (OSError, json.JSONDecodeError):
            continue
    return {
        "research": {
            "state": "ready",
            "unique_sources": len(records),
            "source_counts": dict(sorted(source_counts.items())),
            "records": records,
            "source_states": source_states,
        },
        "adapter": {"state": "ready", "drafts": len(pending_adapters), "archived": len(archived_adapters), "queue": queue},
        "testing": {
            "state": "ready", "strategy_cards": len(cards), "reports": len(testing_reports),
            "history": sorted(testing_reports, key=lambda item: item.get("created_at", ""), reverse=True)[:20],
            "policy": public_policy(), "strategies": read_testing_strategies(project_root, testing_reports),
            "awaiting_adapter": len(pending_adapters),
            "jobs": sorted(jobs, key=lambda item: item.get("updated_at", ""), reverse=True),
        },
        "bot": {
            "state": "not built",
            "live_strategies": 0,
            "open_positions": 0,
        },
        "strategy_cards": cards,
        "adapters": pending_adapters,
        "archived_adapters": archived_adapters,
    }
