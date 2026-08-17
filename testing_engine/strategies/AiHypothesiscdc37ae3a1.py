"""AI hypothesis: BTC mean-reversion rules derived from source context."""

from pandas import DataFrame
import talib.abstract as ta
from freqtrade.strategy import IStrategy


class AiHypothesiscdc37ae3a1(IStrategy):
    timeframe = "1h"
    can_short = False
    startup_candle_count = 34
    minimal_roi = {"0": 10.0}
    stoploss = -0.06
    use_exit_signal = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["mid"] = dataframe["close"].rolling(34).mean()
        dataframe["std"] = dataframe["close"].rolling(34).std()
        dataframe["lower"] = dataframe["mid"] - 2 * dataframe["std"]
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["close"] < dataframe["lower"]) & (dataframe["rsi"] < 33) & (dataframe["volume"] > 0), "enter_long"] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["close"] >= dataframe["mid"]) | (dataframe["rsi"] > 49), "exit_long"] = 1
        return dataframe
