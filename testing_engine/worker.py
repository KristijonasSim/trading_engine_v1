"""Sequential autonomous worker for strategies that passed the Adapter contract."""

from __future__ import annotations

import json
from pathlib import Path

from .__main__ import run_timeframe_comparison
from .policy import candidate_timeframes


TERMINAL = {"baseline_passed", "baseline_failed", "rejected", "nautilus_queue"}


def run_ready(project_root: Path) -> list[str]:
    history = project_root / "data" / "testing" / "history"
    latest: dict[tuple[str, str], tuple[str, str]] = {}
    for path in history.glob("*.json"):
        try:
            report = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        name = report.get("strategy")
        if name and report.get("status"):
            timeframe = str(report.get("timeframe") or "")
            timestamp = str(report.get("created_at", path.name))
            key = (str(name), timeframe)
            if key not in latest or timestamp > latest[key][0]:
                latest[key] = (timestamp, str(report["status"]))
    completed = []
    for strategy in sorted((project_root / "testing_engine" / "strategies").glob("*.py")):
        if strategy.name == "__init__.py":
            continue
        config = project_root / "testing_engine" / "configs" / f"{strategy.stem}.json"
        try:
            suggested = str(json.loads(config.read_text(encoding="utf-8")).get("timeframe", "1h"))
        except (OSError, json.JSONDecodeError):
            suggested = "1h"
        timeframes = candidate_timeframes(suggested)
        missing = tuple(
            timeframe for timeframe in timeframes
            if latest.get((strategy.stem, timeframe), ("", ""))[1] not in TERMINAL
        )
        if not missing:
            continue
        run_timeframe_comparison(strategy.stem, missing)
        completed.append(strategy.stem)
    return completed
