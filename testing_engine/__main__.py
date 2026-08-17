from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from datetime import UTC, datetime
from pathlib import Path

from .policy import ALLOWED_TIMEFRAMES, BTC_PAIR, candidate_timeframes, three_year_timerange

ROOT = Path(__file__).resolve().parent.parent
ENGINE = ROOT / "testing_engine"
HISTORY = ROOT / "data" / "testing" / "history"
JOBS = ROOT / "data" / "testing" / "jobs"


def strategy_paths(name: str) -> tuple[Path, Path]:
    return ENGINE / "strategies" / f"{name}.py", ENGINE / "configs" / f"{name}.json"


def record(name: str, status: str, note: str, metrics: dict[str, str] | None = None, timeframe: str | None = None) -> Path:
    HISTORY.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(UTC)
    suffix = f"_{timeframe}" if timeframe else ""
    path = HISTORY / f"{stamp.strftime('%Y%m%dT%H%M%S%fZ')}_{name}{suffix}_{status}.json"
    path.write_text(json.dumps({"strategy": name, "status": status, "note": note, "metrics": metrics or {}, "pair": BTC_PAIR, "timeframe": timeframe, "timerange": three_year_timerange(), "created_at": stamp.isoformat()}, indent=2) + "\n", encoding="utf-8")
    return path


def update_job(name: str, status: str, message: str, lines: list[str] | None = None) -> Path:
    """Persist the latest state so the local UI can show live progress."""
    JOBS.mkdir(parents=True, exist_ok=True)
    path = JOBS / f"{name}.json"
    try:
        previous = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        previous = {}
    payload = {
        "strategy": name,
        "status": status,
        "message": message,
        "started_at": previous.get("started_at", datetime.now(UTC).isoformat()),
        "updated_at": datetime.now(UTC).isoformat(),
        "lines": (lines if lines is not None else previous.get("lines", []))[-100:],
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def validate(name: str) -> int:
    strategy, config = strategy_paths(name)
    missing = [str(path.relative_to(ROOT)) for path in (strategy, config) if not path.exists()]
    if missing:
        record(name, "blocked", "Missing: " + ", ".join(missing))
        print("Blocked. Missing: " + ", ".join(missing))
        return 1
    source = strategy.read_text(encoding="utf-8")
    if "IStrategy" not in source:
        record(name, "blocked", "Strategy file does not use Freqtrade IStrategy.")
        print("Blocked. Strategy file does not use Freqtrade IStrategy.")
        return 1
    try:
        settings = json.loads(config.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        record(name, "blocked", "Config is not valid JSON.")
        print("Blocked. Config is not valid JSON.")
        return 1
    pair_whitelist = settings.get("exchange", {}).get("pair_whitelist", [])
    if pair_whitelist != [BTC_PAIR]:
        record(name, "blocked", f"Testing Engine only permits {BTC_PAIR}.")
        print(f"Blocked. Testing Engine only permits {BTC_PAIR}.")
        return 1
    allowed_timeframes = {item for values in ALLOWED_TIMEFRAMES.values() for item in values}
    if settings.get("timeframe") not in allowed_timeframes:
        record(name, "blocked", "Config timeframe must be one of: " + ", ".join(sorted(allowed_timeframes)))
        print("Blocked. Config has an unsupported timeframe.")
        return 1
    record(name, "ready_for_baseline", "Files passed local contract check.")
    print("Ready for Freqtrade baseline.")
    return 0


def parse_metrics(output: str) -> dict[str, str]:
    """Extract the four dashboard metrics from Freqtrade's summary table."""
    fields = {
        "pf": r"Profit factor\s*[|│]\s*([^|│\n]+)",
        "cagr": r"CAGR %\s*[|│]\s*([^|│\n]+)",
        "max_drawdown": r"Max % of account underwater\s*[|│]\s*([^|│\n]+)",
        "trades_per_day": r"Total/Daily Avg Trades\s*[|│]\s*[^/|│\n]+/\s*([^|│\n]+)",
    }
    return {
        key: match.group(1).strip()
        for key, pattern in fields.items()
        if (match := re.search(pattern, output, flags=re.IGNORECASE))
    }


def score_metrics(metrics: dict[str, str]) -> float | None:
    """A transparent preliminary 1–10 score; only valid after a real test."""
    required = {"pf", "cagr", "max_drawdown", "trades_per_day"}
    if not required.issubset(metrics):
        return None
    try:
        pf = float(metrics["pf"].replace("%", ""))
        cagr = float(metrics["cagr"].replace("%", ""))
        drawdown = abs(float(metrics["max_drawdown"].replace("%", "")))
        trades_per_day = float(metrics["trades_per_day"].replace("%", ""))
    except ValueError:
        return None
    # PF matters most; drawdown is rewarded for being low. TPD measures sample size,
    # not profitability, so it has deliberately small weight.
    parts = (
        min(max((pf - 0.7) / 1.3, 0), 1) * 0.40,
        min(max(cagr / 50, 0), 1) * 0.25,
        min(max((50 - drawdown) / 40, 0), 1) * 0.25,
        min(max(trades_per_day / 0.3, 0), 1) * 0.10,
    )
    return round(max(1, min(10, sum(parts) * 10)), 1)


def run_baseline(name: str, timerange: str | None, timeframe: str | None = None) -> int:
    """Run one unchanged Adapter strategy through Freqtrade backtesting."""
    update_job(name, "validating", "Checking strategy code and BTC-only test configuration.")
    if validate(name) != 0:
        update_job(name, "blocked", "Strategy failed the local test contract.")
        return 1

    data_dir = ENGINE / "data"
    update_job(name, "checking_data", "Checking downloaded BTC candle data.")
    if not data_dir.exists() or not any(data_dir.iterdir()):
        if shutil.which("docker") is None:
            record(name, "blocked", "Docker is not installed or not on PATH.")
            update_job(name, "blocked", "Docker is required to restore BTC candle data.")
            print("Blocked. Docker is required to restore BTC candle data.")
            return 1
        data_dir.mkdir(parents=True, exist_ok=True)
        download = [
            "docker", "run", "--rm", "-v", f"{ENGINE}:/workspace",
            "freqtradeorg/freqtrade:stable", "download-data", "--userdir", "/workspace",
            "--datadir", "/workspace/data", "--exchange", "binance", "--pairs", BTC_PAIR,
            "--timeframes", "5m", "15m", "1h", "4h", "1d", "--timerange", three_year_timerange(),
        ]
        update_job(name, "downloading_data", "BTC data is missing; restoring the 3-year local dataset.", ["$ " + " ".join(download)])
        download_process = subprocess.Popen(download, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        download_lines: list[str] = []
        assert download_process.stdout is not None
        for line in download_process.stdout:
            download_lines.append(line.rstrip())
            update_job(name, "downloading_data", "Restoring BTC candle data.", download_lines)
        if download_process.wait() != 0:
            record(name, "blocked", "Could not restore BTC candle data.")
            update_job(name, "blocked", "BTC data download failed.", download_lines)
            print("Blocked. BTC data download failed.")
            return 1
        update_job(name, "checking_data", "BTC candle data restored; starting the backtest.", download_lines)
    if shutil.which("docker") is None:
        record(name, "blocked", "Docker is not installed or not on PATH.")
        update_job(name, "blocked", "Docker is not installed or not on PATH.")
        print("Blocked. Docker is required to run Freqtrade.")
        return 1

    _, config = strategy_paths(name)
    try:
        settings = json.loads(config.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        settings = {}
    selected_timeframe = timeframe or str(settings.get("timeframe", ""))
    if selected_timeframe not in {item for values in ALLOWED_TIMEFRAMES.values() for item in values}:
        record(name, "blocked", "Config has an unsupported timeframe.", timeframe=selected_timeframe or None)
        update_job(name, "blocked", "Config has an unsupported timeframe.")
        return 1
    # Keep the Adapter's original config untouched. Freqtrade reads this short-
    # lived comparison config for one timeframe at a time.
    comparison_config = ENGINE / "configs" / f".{name}_{selected_timeframe}.json"
    settings["timeframe"] = selected_timeframe
    comparison_config.write_text(json.dumps(settings, indent=2) + "\n", encoding="utf-8")
    command = [
        "docker", "run", "--rm",
        "-v", f"{ENGINE}:/workspace",
        "freqtradeorg/freqtrade:stable",
        "backtesting",
        "--userdir", "/workspace",
        "--strategy-path", "/workspace/strategies",
        "--config", f"/workspace/configs/{comparison_config.name}",
        "--datadir", "/workspace/data",
        "--strategy", name,
    ]
    command.extend(["--timerange", timerange or three_year_timerange()])
    update_job(name, "running", f"Freqtrade backtest is running on {selected_timeframe}.", ["$ " + " ".join(command)])
    process = subprocess.Popen(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lines: list[str] = []
    try:
        assert process.stdout is not None
        for line in process.stdout:
            lines.append(line.rstrip())
            update_job(name, "running", f"Freqtrade backtest is running on {selected_timeframe}.", lines)
        return_code = process.wait()
    finally:
        comparison_config.unlink(missing_ok=True)
    output = "\n".join(lines).strip()
    tail = output[-1200:] if output else "Freqtrade returned no output."
    status = "baseline_passed" if return_code == 0 else "baseline_failed"
    metrics = parse_metrics(output)
    score = score_metrics(metrics)
    if score is not None:
        metrics["score"] = str(score)
    result = record(name, status, tail, metrics, selected_timeframe)
    update_job(name, status, f"Freqtrade baseline finished on {selected_timeframe}.", lines)
    print(f"{status}: {result}")
    return return_code


def run_timeframe_comparison(name: str, timeframes: tuple[str, ...] | None = None) -> list[str]:
    """Run the correct fixed timeframe set and let the dashboard pick the best."""
    _, config = strategy_paths(name)
    try:
        suggested = str(json.loads(config.read_text(encoding="utf-8")).get("timeframe", "1h"))
    except (OSError, json.JSONDecodeError):
        suggested = "1h"
    selected = timeframes or candidate_timeframes(suggested)
    update_job(name, "queued", f"Testing {', '.join(selected)}; the dashboard will retain the best valid result.")
    completed: list[str] = []
    for index, timeframe in enumerate(selected, start=1):
        update_job(name, "running", f"Testing {timeframe} ({index}/{len(selected)}); comparing eligible timeframes.")
        run_baseline(name, None, timeframe)
        completed.append(timeframe)
    return completed


def main() -> int:
    parser = argparse.ArgumentParser(description="Testing Engine v1")
    commands = parser.add_subparsers(dest="command", required=True)
    validate_parser = commands.add_parser("validate")
    validate_parser.add_argument("strategy")
    run_parser = commands.add_parser("run-baseline", help="Run one unchanged strategy in Freqtrade Docker")
    run_parser.add_argument("strategy")
    run_parser.add_argument("--timerange", help="Optional override; default is the last three years.")
    run_parser.add_argument("--timeframe", help="One allowed timeframe for a targeted backtest.")
    compare_parser = commands.add_parser("run-timeframe-comparison", help="Compare a strategy across its allowed timeframe set")
    compare_parser.add_argument("strategy")
    record_parser = commands.add_parser("record")
    record_parser.add_argument("strategy")
    record_parser.add_argument("status", choices=["baseline_failed", "tuning", "rejected", "nautilus_queue"])
    record_parser.add_argument("note")
    args = parser.parse_args()
    if args.command == "validate":
        return validate(args.strategy)
    if args.command == "run-baseline":
        return run_baseline(args.strategy, args.timerange, args.timeframe)
    if args.command == "run-timeframe-comparison":
        run_timeframe_comparison(args.strategy)
        return 0
    print(record(args.strategy, args.status, args.note))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
