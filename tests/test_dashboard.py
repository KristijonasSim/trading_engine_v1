import json
import tempfile
import unittest
from pathlib import Path

from ui.dashboard import dashboard_data, delete_source, display_title, market_type


class DashboardTests(unittest.TestCase):
    def test_dashboard_counts_unique_saved_sources_and_cards(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            research = root / "data" / "research"
            research.mkdir(parents=True)
            payload = {"records": [
                {"source": "arxiv", "id": "one", "title": "One"},
                {"source": "github", "id": "two", "title": "Two"},
            ]}
            (research / "first.json").write_text(json.dumps(payload), encoding="utf-8")
            cards = root / "strategy_cards"
            cards.mkdir()
            (cards / "one.md").write_text("# Strategy card: One\n- Status: `research`\n", encoding="utf-8")
            data = dashboard_data(root)
            self.assertEqual(data["research"]["unique_sources"], 2)
            self.assertEqual(data["research"]["source_counts"], {"arxiv": 1, "github": 1})
            self.assertEqual(data["testing"]["strategy_cards"], 1)
            self.assertEqual(data["adapter"]["drafts"], 0)

    def test_short_title_and_market_are_simple(self):
        record = {
            "source": "github",
            "id": "SashRajj/Momentum-Based-Crypto-Trading",
            "title": "SashRajj/Momentum-Based-Crypto-Trading",
            "summary": "Crypto trading strategy",
        }
        self.assertEqual(display_title(record), "SashRajj Momentum")
        self.assertEqual(market_type(record), "crypto")

    def test_futures_is_shown_before_crypto(self):
        self.assertEqual(market_type({"title": "Crypto perpetual futures trend"}), "futures")

    def test_newest_harvest_is_first(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            research = root / "data" / "research"
            research.mkdir(parents=True)
            old = {"created_at": "2026-08-10T10:00:00+00:00", "records": [
                {"source": "arxiv", "id": "old", "title": "Old"},
            ]}
            new = {"created_at": "2026-08-11T10:00:00+00:00", "records": [
                {"source": "github", "id": "new", "title": "New"},
            ]}
            (research / "old.json").write_text(json.dumps(old), encoding="utf-8")
            (research / "new.json").write_text(json.dumps(new), encoding="utf-8")
            self.assertEqual(dashboard_data(root)["research"]["records"][0]["id"], "new")

    def test_deleted_source_stays_hidden(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            research = root / "data" / "research"
            research.mkdir(parents=True)
            payload = {"records": [{"source": "github", "id": "ignore-me", "title": "Ignore"}]}
            (research / "sources.json").write_text(json.dumps(payload), encoding="utf-8")
            delete_source(root, "github", "ignore-me")
            self.assertEqual(dashboard_data(root)["research"]["unique_sources"], 0)


if __name__ == "__main__":
    unittest.main()
