"""AI hypothesis: BTC price-action breakout rules derived from source context."""

from pandas import DataFrame
import talib.abstract as ta
from freqtrade.strategy import IStrategy


class AiHypothesis9c673c6a1c(IStrategy):
    timeframe = "5m"
    can_short = False
    startup_candle_count = 23
    minimal_roi = {"0": 10.0}
    stoploss = -0.08
    use_exit_signal = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["range_high"] = dataframe["high"].rolling(22).max().shift(1)
        dataframe["ema_exit"] = ta.EMA(dataframe, timeperiod=14)
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["close"] > dataframe["range_high"]) & (dataframe["rsi"] > 55) & (dataframe["volume"] > 0), "enter_long"] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["close"] < dataframe["ema_exit"]) | (dataframe["rsi"] < 49), "exit_long"] = 1
        return dataframe
