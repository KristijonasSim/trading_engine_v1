"""AI hypothesis: BTC mean-reversion rules derived from source context."""

from pandas import DataFrame
import talib.abstract as ta
from freqtrade.strategy import IStrategy


class AiHypothesisf7975fc7ba(IStrategy):
    timeframe = "1h"
    can_short = False
    startup_candle_count = 24
    minimal_roi = {"0": 10.0}
    stoploss = -0.03
    use_exit_signal = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["mid"] = dataframe["close"].rolling(24).mean()
        dataframe["std"] = dataframe["close"].rolling(24).std()
        dataframe["lower"] = dataframe["mid"] - 2 * dataframe["std"]
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["close"] < dataframe["lower"]) & (dataframe["rsi"] < 42) & (dataframe["volume"] > 0), "enter_long"] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["close"] >= dataframe["mid"]) | (dataframe["rsi"] > 50), "exit_long"] = 1
        return dataframe
