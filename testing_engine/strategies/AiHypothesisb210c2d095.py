"""AI hypothesis: BTC price-action breakout rules derived from source context."""

from pandas import DataFrame
import talib.abstract as ta
from freqtrade.strategy import IStrategy


class AiHypothesisb210c2d095(IStrategy):
    timeframe = "1h"
    can_short = False
    startup_candle_count = 46
    minimal_roi = {"0": 10.0}
    stoploss = -0.09
    use_exit_signal = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["range_high"] = dataframe["high"].rolling(45).max().shift(1)
        dataframe["ema_exit"] = ta.EMA(dataframe, timeperiod=8)
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["close"] > dataframe["range_high"]) & (dataframe["rsi"] > 60) & (dataframe["volume"] > 0), "enter_long"] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["close"] < dataframe["ema_exit"]) | (dataframe["rsi"] < 46), "exit_long"] = 1
        return dataframe
