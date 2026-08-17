"""BTC 30-day long/cash momentum, directly based on the saved source rules."""

from pandas import DataFrame
from freqtrade.strategy import IStrategy


class BtcThirtyDayMomentum(IStrategy):
    timeframe = "1d"
    can_short = False
    startup_candle_count = 31
    minimal_roi = {"0": 10.0}
    stoploss = -0.25
    use_exit_signal = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["return_30d"] = dataframe["close"] / dataframe["close"].shift(30) - 1
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[dataframe["return_30d"] > 0, "enter_long"] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[dataframe["return_30d"] <= 0, "exit_long"] = 1
        return dataframe
