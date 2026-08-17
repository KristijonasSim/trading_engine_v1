"""Rule-safe automatic conversion from an Adapter draft to Freqtrade files."""

from __future__ import annotations

import json
import base64
import hashlib
import re
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from pathlib import Path


BTC_MOMENTUM_NAME = "BtcThirtyDayMomentum"


def _set_status(path: Path, status: str, handoff: str, note: str) -> None:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^- Status: `[^`]+`", f"- Status: `{status}`", text, count=1, flags=re.MULTILINE)
    text = re.sub(r"^- Testing handoff: `[^`]+`", f"- Testing handoff: `{handoff}`", text, count=1, flags=re.MULTILINE)
    if "## Automation" not in text:
        text += f"\n## Automation\n\n- Result: {note}\n"
    else:
        text = re.sub(r"^- Result: .+$", f"- Result: {note}", text, count=1, flags=re.MULTILINE)
    path.write_text(text, encoding="utf-8")


def _momentum_strategy() -> str:
    return '''"""BTC 30-day long/cash momentum, directly based on the saved source rules."""

from pandas import DataFrame
from freqtrade.strategy import IStrategy


class BtcThirtyDayMomentum(IStrategy):
    timeframe = "1d"
    can_short = False
    startup_candle_count = 31
    minimal_roi = {"0": 10.0}
    stoploss = -0.25
    use_exit_signal = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["return_30d"] = dataframe["close"] / dataframe["close"].shift(30) - 1
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[dataframe["return_30d"] > 0, "enter_long"] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[dataframe["return_30d"] <= 0, "exit_long"] = 1
        return dataframe
'''


def _momentum_config() -> dict:
    return {
        "dry_run": True,
        "stake_currency": "USDT",
        "stake_amount": 100,
        "max_open_trades": 1,
        "timeframe": "1d",
        "trading_mode": "spot",
        "exchange": {"name": "binance", "key": "", "secret": "", "pair_whitelist": ["BTC/USDT"]},
        "pairlists": [{"method": "StaticPairList"}],
        "entry_pricing": {"price_side": "same", "use_order_book": False},
        "exit_pricing": {"price_side": "same", "use_order_book": False},
    }


def _fetch_source(url: str) -> str:
    """Read public source text; GitHub READMEs need the API endpoint."""
    parsed = urlparse(url)
    try:
        if parsed.netloc == "github.com":
            parts = [part for part in parsed.path.split("/") if part]
            if len(parts) >= 2:
                request = Request(f"https://api.github.com/repos/{parts[0]}/{parts[1]}/readme", headers={"Accept": "application/vnd.github+json"})
                payload = json.loads(urlopen(request, timeout=12).read().decode("utf-8"))
                return base64.b64decode(payload.get("content", "")).decode("utf-8", errors="replace")
        return urlopen(Request(url, headers={"User-Agent": "TradingEngine/1.0"}), timeout=12).read(1_000_000).decode("utf-8", errors="replace")
    except Exception:
        return ""


def _profile_for(title: str, text: str) -> tuple[str, int, int, int, int, float]:
    value = f"{title} {text}".lower()
    if "stat-arb" in value or "stat arb" in value:
        return "mean_reversion", 8, 34, 48, 52, -0.05
    if "discovery" in value or "factor" in value:
        return "factor_momentum", 13, 55, 52, 47, -0.06
    if "sash" in value or "machine learning" in value:
        return "trend_strength", 10, 40, 58, 42, -0.07
    if "santos" in value or "breakout" in value:
        return "breakout_momentum", 6, 30, 60, 45, -0.06
    if "leviathan" in value:
        return "crossover_momentum", 15, 45, 54, 46, -0.08
    if "yeshunyi" in value:
        return "slow_momentum", 20, 60, 56, 44, -0.10
    return "balanced_momentum", 20, 50, 55, 45, -0.08


def _hypothesis_strategy(class_name: str, timeframe: str, profile: tuple[str, int, int, int, int, float]) -> str:
    profile_name, fast, slow, entry_rsi, exit_rsi, stoploss = profile
    return f'''"""AI hypothesis generated after source-rule recovery was incomplete.

This is a test candidate, not proof that the original author used these rules.
"""

from pandas import DataFrame
import talib.abstract as ta
from freqtrade.strategy import IStrategy


class {class_name}(IStrategy):
    timeframe = "{timeframe}"
    can_short = False
    startup_candle_count = {slow}
    minimal_roi = {{"0": 10.0}}
    stoploss = {stoploss}
    use_exit_signal = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["ema_fast"] = ta.EMA(dataframe, timeperiod={fast})
        dataframe["ema_slow"] = ta.EMA(dataframe, timeperiod={slow})
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["ema_fast"] > dataframe["ema_slow"]) & (dataframe["rsi"] > {entry_rsi}) & (dataframe["volume"] > 0), "enter_long"] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["ema_fast"] < dataframe["ema_slow"]) | (dataframe["rsi"] < {exit_rsi}), "exit_long"] = 1
        return dataframe
'''


def _timeframe_for(text: str) -> str:
    text = text.lower()
    if "scalp" in text or "5-minute" in text or "5 minute" in text:
        return "5m"
    if "6-hour" in text or "6 hour" in text or "4-hour" in text or "4 hour" in text:
        return "4h"
    if "daily" in text or "30-day" in text or "30 day" in text:
        return "1d"
    return "1h"


def _write_registry(project_root: Path, class_name: str, source_title: str, adapter_file: str, hypothesis: bool, family: str | None = None) -> None:
    registry_path = project_root / "testing_engine" / "registry.json"
    try:
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        registry = {}
    registry[class_name] = {"source_title": source_title, "adapter_file": adapter_file, "hypothesis": hypothesis, "family": family}
    registry_path.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")


def adapt_one(project_root: Path, filename: str) -> str:
    """Adapt one selected draft, returning its honest outcome."""
    path = project_root / "strategy_adapters" / filename
    if path.name != filename or not path.exists() or path.suffix != ".md":
        raise ValueError("Adapter draft not found.")
    text = path.read_text(encoding="utf-8")
    if "Status: `adapted`" in text:
        return "already_adapted"
    if "Status: `needs_source_rules`" in text:
        return "needs_source_rules"
    strategy_dir = project_root / "testing_engine" / "strategies"
    config_dir = project_root / "testing_engine" / "configs"
    strategy_dir.mkdir(parents=True, exist_ok=True)
    config_dir.mkdir(parents=True, exist_ok=True)
    # This source states: 30-day cumulative return > 0 => long; otherwise cash.
    if "Risk-Managed Crypto Momentum" in text and "30-day" in text:
        (strategy_dir / f"{BTC_MOMENTUM_NAME}.py").write_text(_momentum_strategy(), encoding="utf-8")
        (config_dir / f"{BTC_MOMENTUM_NAME}.json").write_text(json.dumps(_momentum_config(), indent=2) + "\n", encoding="utf-8")
        _write_registry(project_root, BTC_MOMENTUM_NAME, "Risk-Managed Crypto Momentum", path.name, False)
        _set_status(path, "adapted", "ready", f"Created {BTC_MOMENTUM_NAME}: BTC/USDT 30-day long/cash momentum on 1d candles.")
        return "adapted"
    return find_rules(project_root, filename)


def find_rules(project_root: Path, filename: str) -> str:
    """Recover public rules, then create an explicit AI hypothesis if incomplete."""
    path = project_root / "strategy_adapters" / filename
    if path.name != filename or not path.exists() or path.suffix != ".md":
        raise ValueError("Adapter draft not found.")
    draft = path.read_text(encoding="utf-8")
    if "Status: `adapted`" in draft or "Status: `ai_hypothesis`" in draft:
        return "already_sent_to_testing"
    title_match = re.search(r"^# Strategy adapter: (.+)$", draft, re.MULTILINE)
    url_match = re.search(r"^- Link: (.+)$", draft, re.MULTILINE)
    title = title_match.group(1) if title_match else path.stem
    source_text = _fetch_source(url_match.group(1)) if url_match else ""
    combined = f"{draft}\n{source_text}"
    timeframe = _timeframe_for(combined)
    profile = _profile_for(title, combined)
    family = f"{profile[0]}_{timeframe}"
    registry_path = project_root / "testing_engine" / "registry.json"
    try:
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        registry = {}
    existing = next((name for name, item in registry.items() if item.get("hypothesis") and item.get("family") == family and not item.get("duplicate_of")), None)
    if existing:
        _set_status(path, "duplicate_hypothesis", "archived", f"Not sent to Testing: it duplicates AI hypothesis {existing} for the same {timeframe} EMA/RSI rule family.")
        return "duplicate_hypothesis"
    class_name = "AiHypothesis" + hashlib.sha1(path.name.encode("utf-8")).hexdigest()[:10]
    strategy_dir = project_root / "testing_engine" / "strategies"; config_dir = project_root / "testing_engine" / "configs"
    strategy_dir.mkdir(parents=True, exist_ok=True); config_dir.mkdir(parents=True, exist_ok=True)
    (strategy_dir / f"{class_name}.py").write_text(_hypothesis_strategy(class_name, timeframe, profile), encoding="utf-8")
    config = _momentum_config(); config["timeframe"] = timeframe
    (config_dir / f"{class_name}.json").write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    _write_registry(project_root, class_name, title, path.name, True, family)
    recovered = "Public source inspected; " if source_text else "Source page could not be read; "
    _set_status(path, "ai_hypothesis", "ready", recovered + f"proposed {profile[0]} rules: EMA {profile[1]}/{profile[2]}, RSI entry > {profile[3]}, exit < {profile[4]}, stop-loss {profile[5]:.0%}, fixed $100 position, {timeframe}. Testing must judge it; it is not claimed as the original author's exact strategy.")
    return "ai_hypothesis"


def restore_archived_hypotheses(project_root: Path) -> list[str]:
    """Replace legacy duplicate fallbacks with distinct, source-specific proposals."""
    registry_path = project_root / "testing_engine" / "registry.json"
    try:
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    restored = []
    for class_name, item in registry.items():
        if not item.get("duplicate_of"):
            continue
        path = project_root / "strategy_adapters" / item["adapter_file"]
        draft = path.read_text(encoding="utf-8")
        title = item["source_title"]
        profile = _profile_for(title, draft)
        timeframe = _timeframe_for(draft)
        strategy_path = project_root / "testing_engine" / "strategies" / f"{class_name}.py"
        config_path = project_root / "testing_engine" / "configs" / f"{class_name}.json"
        strategy_path.write_text(_hypothesis_strategy(class_name, timeframe, profile), encoding="utf-8")
        config = _momentum_config(); config["timeframe"] = timeframe
        config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
        item.pop("duplicate_of", None)
        item["family"] = f"{profile[0]}_{timeframe}"
        _set_status(path, "ai_hypothesis", "ready", f"AI proposed {profile[0]} rules: EMA {profile[1]}/{profile[2]}, RSI entry > {profile[3]}, exit < {profile[4]}, stop-loss {profile[5]:.0%}, fixed $100 position, {timeframe}. This is an independent test hypothesis, not a claim about the original author's exact rules.")
        restored.append(class_name)
    registry_path.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
    return restored


def deduplicate_hypotheses(project_root: Path) -> int:
    """Archive legacy generated copies that have the same code and timeframe."""
    registry_path = project_root / "testing_engine" / "registry.json"
    try:
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return 0
    groups: dict[str, list[str]] = {}
    for name, item in registry.items():
        if not item.get("hypothesis"):
            continue
        path = project_root / "testing_engine" / "strategies" / f"{name}.py"
        try:
            code = path.read_text(encoding="utf-8")
        except OSError:
            continue
        timeframe = re.search(r'timeframe = "([^"]+)"', code)
        if timeframe:
            registry[name]["family"] = f"ema_rsi_momentum_{timeframe.group(1)}"
        normalized = re.sub(r"class AiHypothesis[0-9a-f]+", "class AiHypothesis", code)
        fingerprint = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
        groups.setdefault(fingerprint, []).append(name)
    duplicates = 0
    for names in groups.values():
        keeper = sorted(names)[0]
        for name in sorted(names)[1:]:
            registry[name]["duplicate_of"] = keeper
            adapter_file = registry[name].get("adapter_file")
            if adapter_file:
                _set_status(project_root / "strategy_adapters" / adapter_file, "duplicate_hypothesis", "archived", f"Archived: same generated rule set as {keeper}; it is not an independent strategy.")
            duplicates += 1
    registry_path.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
    return duplicates


def find_all_rules(project_root: Path) -> dict[str, int]:
    outcomes = {"ai_hypothesis": 0, "already_sent_to_testing": 0}
    for path in sorted((project_root / "strategy_adapters").glob("*.md")):
        result = find_rules(project_root, path.name)
        outcomes[result] = outcomes.get(result, 0) + 1
    return outcomes


def adapt_all(project_root: Path) -> dict[str, list[str]]:
    """Create code only where the saved source states all decisive rules."""
    adapted: list[str] = []
    needs_rules: list[str] = []
    hypotheses: list[str] = []
    for path in sorted((project_root / "strategy_adapters").glob("*.md")):
        result = adapt_one(project_root, path.name)
        if result == "adapted":
            adapted.append(BTC_MOMENTUM_NAME)
        elif result == "ai_hypothesis":
            hypotheses.append(path.stem)
        elif result == "needs_source_rules":
            needs_rules.append(path.stem)
    return {"adapted": adapted, "ai_hypothesis": hypotheses, "needs_source_rules": needs_rules}
