import tempfile
import unittest
from pathlib import Path

from strategy_adapter.automatic import BTC_MOMENTUM_NAME, adapt_all


class AutomaticAdapterTests(unittest.TestCase):
    def test_only_explicit_momentum_rules_create_test_code(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); drafts = root / "strategy_adapters"; drafts.mkdir()
            (drafts / "momentum.md").write_text("# Strategy adapter: Risk-Managed Crypto Momentum\n- Status: `draft`\n- Testing handoff: `blocked`\nA 30-day long/cash rule.\n", encoding="utf-8")
            (drafts / "unknown.md").write_text("# Strategy adapter: Unknown\n- Status: `draft`\n- Testing handoff: `blocked`\n", encoding="utf-8")
            result = adapt_all(root)
            self.assertEqual(result["adapted"], [BTC_MOMENTUM_NAME])
            self.assertEqual(result["needs_source_rules"], [])
            self.assertEqual(result["ai_hypothesis"], ["unknown"])
            self.assertTrue((root / "testing_engine" / "strategies" / f"{BTC_MOMENTUM_NAME}.py").exists())
