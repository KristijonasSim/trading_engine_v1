import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from testing_engine import __main__ as engine


class TestingEngineTests(unittest.TestCase):
    def test_freqtrade_summary_metrics_are_parsed(self):
        output = """| Profit factor | 1.42 |
| CAGR % | 18.50% |
| Max % of account underwater | 12.30% |
| Total/Daily Avg Trades | 120 / 1.33 |"""
        self.assertEqual(engine.parse_metrics(output), {"pf": "1.42", "cagr": "18.50%", "max_drawdown": "12.30%", "trades_per_day": "1.33"})

    def test_unicode_freqtrade_summary_metrics_are_parsed(self):
        output = "│ Profit factor │ 1.69 │\n│ CAGR % │ 2.78% │\n│ Max % of account underwater │ 3.65% │\n│ Total/Daily Avg Trades │ 54 / 0.05 │"
        self.assertEqual(engine.parse_metrics(output), {"pf": "1.69", "cagr": "2.78%", "max_drawdown": "3.65%", "trades_per_day": "0.05"})

    def test_score_requires_all_metrics_and_stays_on_one_to_ten(self):
        self.assertIsNone(engine.score_metrics({"pf": "2.0"}))
        score = engine.score_metrics({"pf": "2.0", "cagr": "50%", "max_drawdown": "10%", "trades_per_day": "1.0"})
        self.assertEqual(score, 10)

    def test_missing_strategy_is_blocked_and_saved(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(engine, "ROOT", root), patch.object(engine, "ENGINE", root / "testing_engine"), patch.object(engine, "HISTORY", root / "history"):
                self.assertEqual(engine.validate("MissingStrategy"), 1)
                report = next((root / "history").glob("*.json"))
                self.assertEqual(json.loads(report.read_text(encoding="utf-8"))["status"], "blocked")

    def test_freqtrade_contract_is_ready_only_with_code_and_config(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            strategy_dir = root / "testing_engine" / "strategies"
            config_dir = root / "testing_engine" / "configs"
            strategy_dir.mkdir(parents=True)
            config_dir.mkdir(parents=True)
            (strategy_dir / "ReadyStrategy.py").write_text("from freqtrade.strategy import IStrategy\nclass ReadyStrategy(IStrategy): pass\n", encoding="utf-8")
            (config_dir / "ReadyStrategy.json").write_text('{"timeframe": "5m", "exchange": {"pair_whitelist": ["BTC/USDT"]}}', encoding="utf-8")
            with patch.object(engine, "ROOT", root), patch.object(engine, "ENGINE", root / "testing_engine"), patch.object(engine, "HISTORY", root / "history"):
                self.assertEqual(engine.validate("ReadyStrategy"), 0)
                report = next((root / "history").glob("*.json"))
                self.assertEqual(json.loads(report.read_text(encoding="utf-8"))["status"], "ready_for_baseline")

    def test_comparison_uses_day_trading_timeframes_for_a_day_strategy(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            configs = root / "testing_engine" / "configs"
            configs.mkdir(parents=True)
            (configs / "Example.json").write_text('{"timeframe": "1h"}', encoding="utf-8")
            with patch.object(engine, "ENGINE", root / "testing_engine"), patch.object(engine, "update_job"), patch.object(engine, "run_baseline", return_value=0) as run:
                self.assertEqual(engine.run_timeframe_comparison("Example"), ["1h", "4h", "1d"])
                self.assertEqual([call.args[2] for call in run.call_args_list], ["1h", "4h", "1d"])
