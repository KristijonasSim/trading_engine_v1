import tempfile
import unittest
from pathlib import Path

from research_engine.cards import make_card, write_card
from research_engine.collectors import classify_market, clean_text, expand_query, is_strategy_source, new_result_file


class ResearchEngineTests(unittest.TestCase):
    def test_clean_text_removes_html(self):
        self.assertEqual(clean_text("  <p>Crypto &amp; trend</p> "), "Crypto & trend")

    def test_result_file_is_safe(self):
        filename = new_result_file("Crypto momentum!", "crossref")
        self.assertTrue(filename.endswith("_crossref_crypto-momentum.json"))

    def test_orb_is_expanded_and_unrelated_source_is_rejected(self):
        query = expand_query("ORB")
        self.assertEqual(query, "open range breakout trading strategy")
        self.assertFalse(is_strategy_source({"title": "ORB: An Open Radio Buoy"}, query))
        stock_orb = {"title": "Opening Range Breakout intraday trading with yfinance"}
        self.assertTrue(is_strategy_source(stock_orb, query))
        self.assertEqual(classify_market(stock_orb), "stocks")

    def test_card_has_unknown_rules(self):
        record = {
            "source": "arxiv",
            "id": "1234.5678",
            "title": "Example strategy",
            "url": "https://example.com",
            "authors": ["A. Researcher"],
            "published": "2026-01-01",
            "summary": "A test source.",
            "license": "Check source",
        }
        self.assertIn("- Entry: `unknown`", make_card(record))
        with tempfile.TemporaryDirectory() as directory:
            path = write_card(record, Path(directory))
            self.assertTrue(path.exists())
            self.assertIn("Example strategy", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
