"""AI hypothesis: BTC mean-reversion rules derived from source context."""

from pandas import DataFrame
import talib.abstract as ta
from freqtrade.strategy import IStrategy


class AiHypothesisdc5e324522(IStrategy):
    timeframe = "1d"
    can_short = False
    startup_candle_count = 59
    minimal_roi = {"0": 10.0}
    stoploss = -0.02
    use_exit_signal = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["mid"] = dataframe["close"].rolling(59).mean()
        dataframe["std"] = dataframe["close"].rolling(59).std()
        dataframe["lower"] = dataframe["mid"] - 2 * dataframe["std"]
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["close"] < dataframe["lower"]) & (dataframe["rsi"] < 39) & (dataframe["volume"] > 0), "enter_long"] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["close"] >= dataframe["mid"]) | (dataframe["rsi"] > 49), "exit_long"] = 1
        return dataframe
