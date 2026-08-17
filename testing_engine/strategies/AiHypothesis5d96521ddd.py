"""AI hypothesis generated after source-rule recovery was incomplete.

This is a test candidate, not proof that the original author used these rules.
"""

from pandas import DataFrame
import talib.abstract as ta
from freqtrade.strategy import IStrategy


class AiHypothesis5d96521ddd(IStrategy):
    timeframe = "1d"
    can_short = False
    startup_candle_count = 43
    minimal_roi = {"0": 10.0}
    stoploss = -0.04
    use_exit_signal = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["ema_fast"] = ta.EMA(dataframe, timeperiod=13)
        dataframe["ema_slow"] = ta.EMA(dataframe, timeperiod=43)
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["ema_fast"] > dataframe["ema_slow"]) & (dataframe["rsi"] > 63) & (dataframe["volume"] > 0), "enter_long"] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["ema_fast"] < dataframe["ema_slow"]) | (dataframe["rsi"] < 36), "exit_long"] = 1
        return dataframe
