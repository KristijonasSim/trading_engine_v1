"""Sequential autonomous worker for strategies that passed the Adapter contract."""

from __future__ import annotations

import json
from pathlib import Path

from .__main__ import read_shared_history, run_timeframe_comparison
from .policy import candidate_timeframes


TERMINAL = {"baseline_passed", "baseline_failed", "rejected", "nautilus_queue"}


def run_ready(project_root: Path, force: bool = False) -> list[str]:
    latest: dict[tuple[str, str], tuple[str, str]] = {}
    for report in read_shared_history(project_root):
        name = report.get("strategy")
        if name and report.get("status"):
            timeframe = str(report.get("timeframe") or "")
            timestamp = str(report.get("created_at", ""))
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
        missing = timeframes if force else tuple(
            timeframe for timeframe in timeframes
            if latest.get((strategy.stem, timeframe), ("", ""))[1] not in TERMINAL
        )
        if not missing:
            continue
        run_timeframe_comparison(strategy.stem, missing)
        completed.append(strategy.stem)
    return completed
