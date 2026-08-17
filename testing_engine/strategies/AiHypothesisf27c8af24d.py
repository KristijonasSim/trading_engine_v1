"""AI hypothesis: BTC trend rules gated by a volatility regime."""

from pandas import DataFrame
import talib.abstract as ta
from freqtrade.strategy import IStrategy


class AiHypothesisf27c8af24d(IStrategy):
    timeframe = "1h"
    can_short = False
    startup_candle_count = 51
    minimal_roi = {"0": 10.0}
    stoploss = -0.08
    use_exit_signal = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["ema_fast"] = ta.EMA(dataframe, timeperiod=13)
        dataframe["ema_slow"] = ta.EMA(dataframe, timeperiod=51)
        dataframe["atr_pct"] = ta.ATR(dataframe, timeperiod=14) / dataframe["close"]
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["ema_fast"] > dataframe["ema_slow"]) & (dataframe["atr_pct"] > 0.002) & (dataframe["rsi"] > 55) & (dataframe["volume"] > 0), "enter_long"] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["ema_fast"] < dataframe["ema_slow"]) | (dataframe["rsi"] < 39), "exit_long"] = 1
        return dataframe
