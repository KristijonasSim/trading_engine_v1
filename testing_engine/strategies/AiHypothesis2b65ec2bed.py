"""AI hypothesis generated after source-rule recovery was incomplete.

This is a test candidate, not proof that the original author used these rules.
"""

from pandas import DataFrame
import talib.abstract as ta
from freqtrade.strategy import IStrategy


class AiHypothesis2b65ec2bed(IStrategy):
    timeframe = "1h"
    can_short = False
    startup_candle_count = 44
    minimal_roi = {"0": 10.0}
    stoploss = -0.09
    use_exit_signal = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["ema_fast"] = ta.EMA(dataframe, timeperiod=14)
        dataframe["ema_slow"] = ta.EMA(dataframe, timeperiod=44)
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["ema_fast"] > dataframe["ema_slow"]) & (dataframe["rsi"] > 46) & (dataframe["volume"] > 0), "enter_long"] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["ema_fast"] < dataframe["ema_slow"]) | (dataframe["rsi"] < 42), "exit_long"] = 1
        return dataframe
