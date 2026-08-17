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

    def test_stock_momentum_title_is_not_mislabelled_as_crypto(self):
        record = {
            "source": "crossref",
            "id": "stock-momentum",
            "title": "Comparison of Cross-sectional Momentum Strategy and Time-Series Momentum Strategy",
            "summary": "A stock investing study.",
        }
        self.assertEqual(display_title(record), record["title"])
        self.assertEqual(market_type(record), "stocks")

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

    def test_actionable_ideas_come_before_tested_and_out_of_scope_sources(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            research = root / "data" / "research"
            research.mkdir(parents=True)
            payload = {
                "created_at": "2026-08-17T10:00:00+00:00",
                "records": [
                    {"source": "github", "id": "tested", "title": "Tested crypto strategy", "url": "https://example.test/tested"},
                    {"source": "github", "id": "active", "title": "Active crypto strategy", "url": "https://example.test/active"},
                    {"source": "arxiv", "id": "other", "title": "A recommendation paper", "url": "https://example.test/other"},
                ],
            }
            (research / "sources.json").write_text(json.dumps(payload), encoding="utf-8")
            adapters = root / "strategy_adapters"
            adapters.mkdir()
            (adapters / "tested.md").write_text(
                "# Strategy adapter: Tested\n- Link: https://example.test/tested\n- Status: `ai_hypothesis`\n",
                encoding="utf-8",
            )
            ids = [item["id"] for item in dashboard_data(root)["research"]["records"]]
            self.assertEqual(ids, ["active", "tested", "other"])

    def test_stock_and_forex_ideas_are_actionable_for_btc_translation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            research = root / "data" / "research"
            research.mkdir(parents=True)
            payload = {"records": [
                {"source": "crossref", "id": "other", "title": "A recommendation paper"},
                {"source": "crossref", "id": "stock", "title": "A stock momentum trading strategy"},
                {"source": "crossref", "id": "forex", "title": "A forex trend trading strategy"},
            ]}
            (research / "sources.json").write_text(json.dumps(payload), encoding="utf-8")
            ids = [item["id"] for item in dashboard_data(root)["research"]["records"]]
            self.assertEqual(ids, ["stock", "forex", "other"])

    def test_unspecified_momentum_strategy_is_a_general_market_idea(self):
        record = {"title": "The Lazy Man's Momentum Strategy"}
        self.assertEqual(market_type(record), "general")

    def test_price_action_and_technical_analysis_are_general_market_ideas(self):
        self.assertEqual(market_type({"title": "Algorithmic trading using price action strategies"}), "general")
        self.assertEqual(market_type({"title": "Automating technical analysis"}), "general")


if __name__ == "__main__":
    unittest.main()
