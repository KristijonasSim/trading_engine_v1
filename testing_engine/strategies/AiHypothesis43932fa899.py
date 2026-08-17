"""AI hypothesis: BTC trend rules gated by a volatility regime."""

from pandas import DataFrame
import talib.abstract as ta
from freqtrade.strategy import IStrategy


class AiHypothesis43932fa899(IStrategy):
    timeframe = "1d"
    can_short = False
    startup_candle_count = 40
    minimal_roi = {"0": 10.0}
    stoploss = -0.1
    use_exit_signal = True

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe["ema_fast"] = ta.EMA(dataframe, timeperiod=11)
        dataframe["ema_slow"] = ta.EMA(dataframe, timeperiod=40)
        dataframe["atr_pct"] = ta.ATR(dataframe, timeperiod=14) / dataframe["close"]
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["ema_fast"] > dataframe["ema_slow"]) & (dataframe["atr_pct"] > 0.002) & (dataframe["rsi"] > 58) & (dataframe["volume"] > 0), "enter_long"] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        dataframe.loc[(dataframe["ema_fast"] < dataframe["ema_slow"]) | (dataframe["rsi"] < 52), "exit_long"] = 1
        return dataframe
