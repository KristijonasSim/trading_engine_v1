import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from testing_engine import worker


class TestingWorkerTests(unittest.TestCase):
    def test_terminal_strategy_is_not_run_again(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            strategies = root / "testing_engine" / "strategies"; strategies.mkdir(parents=True)
            (strategies / "Done.py").write_text("", encoding="utf-8")
            history = root / "data" / "testing" / "history"; history.mkdir(parents=True)
            configs = root / "testing_engine" / "configs"; configs.mkdir()
            (configs / "Done.json").write_text('{"timeframe": "1h"}', encoding="utf-8")
            for timeframe in ("1h", "4h", "1d"):
                (history / f"done-{timeframe}.json").write_text(json.dumps({"strategy": "Done", "timeframe": timeframe, "status": "baseline_passed"}), encoding="utf-8")
            with patch.object(worker, "run_timeframe_comparison") as run:
                self.assertEqual(worker.run_ready(root), [])
                run.assert_not_called()

    def test_newest_terminal_event_wins_over_old_ready_event(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); strategies = root / "testing_engine" / "strategies"; strategies.mkdir(parents=True)
            (strategies / "Done.py").write_text("", encoding="utf-8")
            history = root / "data" / "testing" / "history"; history.mkdir(parents=True)
            configs = root / "testing_engine" / "configs"; configs.mkdir()
            (configs / "Done.json").write_text('{"timeframe": "1h"}', encoding="utf-8")
            for timeframe in ("1h", "4h", "1d"):
                (history / f"old-{timeframe}.json").write_text(json.dumps({"strategy": "Done", "timeframe": timeframe, "status": "ready_for_baseline", "created_at": "2026-01-01T00:00:00Z"}), encoding="utf-8")
                (history / f"new-{timeframe}.json").write_text(json.dumps({"strategy": "Done", "timeframe": timeframe, "status": "baseline_passed", "created_at": "2026-01-02T00:00:00Z"}), encoding="utf-8")
            with patch.object(worker, "run_timeframe_comparison") as run:
                self.assertEqual(worker.run_ready(root), [])
                run.assert_not_called()
