# Testing Engine v1

Primary suite: Freqtrade in Docker.

## First-stage market policy

- Pair: BTC/USDT only.
- History: the most recent three calendar years.
- Scalping candidates are compared on both 5m and 15m.
- Day/swing candidates are compared on 1h, 4h and 1d.
- Testing Engine keeps the best valid timeframe result by its 1–10 score.
- Results shown: Profit Factor (PF), CAGR, maximum drawdown (DD), and trades per day (TPD).
- A preliminary 1–10 score is calculated only when a real backtest returned all four metrics.
  It weighs PF 40%, CAGR 25%, lower DD 25%, and enough trades/day 10%.

## Rules

- Test the Adapter baseline before changing settings.
- Save every run and every setting tried.
- Tune only approved fields with a fixed run limit.
- Test the final version on hidden newer data.
- Run Freqtrade look-ahead and recursive checks.
- Reject strategies that fail. Do not silently retry them forever.
- Only Freqtrade survivors move to NautilusTrader.
- Backtests use Docker and never receive exchange keys.

## Strategy contract

The Adapter must create a Freqtrade `IStrategy` Python file under `testing_engine/strategies/`.
It must also provide a config file under `testing_engine/configs/`.
Downloaded candle data stays in `testing_engine/data/` and is never committed.
The config must whitelist only `BTC/USDT` and use one of the approved timeframes.

The first test restores the BTC dataset automatically if it is missing. There is no
separate download step in the dashboard.

## Commands

```bash
python3 -m testing_engine validate StrategyName
python3 -m testing_engine run-baseline StrategyName
python3 -m testing_engine run-timeframe-comparison StrategyName
python3 -m testing_engine record StrategyName baseline_failed "Missing stop-loss rule"
```

`validate` is safe and local. It checks that the expected files exist before Freqtrade is run.
`run-baseline` runs the Adapter's unchanged code in the official Freqtrade Docker image,
then records the outcome and Freqtrade output in local test history.
`run-timeframe-comparison` runs the relevant fixed timeframe set and records each result;
the dashboard displays the best valid one.
