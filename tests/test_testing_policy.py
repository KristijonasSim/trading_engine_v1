import unittest
from datetime import date

from testing_engine.policy import BTC_PAIR, candidate_timeframes, public_policy, three_year_timerange


class TestingPolicyTests(unittest.TestCase):
    def test_three_year_timerange_is_exact(self):
        self.assertEqual(three_year_timerange(date(2026, 8, 17)), "20230817-20260817")
        self.assertEqual(BTC_PAIR, "BTC/USDT")

    def test_timeframe_comparison_uses_the_correct_group(self):
        self.assertEqual(candidate_timeframes("5m"), ("5m", "15m"))
        self.assertEqual(candidate_timeframes("15m"), ("5m", "15m"))
        self.assertEqual(candidate_timeframes("1h"), ("1h", "4h", "1d"))

    def test_first_stage_thresholds_are_published(self):
        self.assertEqual(public_policy()["promotion_rules"], {"min_profit_factor": 2.0, "min_trades_per_day": 0.2})
