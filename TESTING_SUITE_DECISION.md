# Testing Suite Decision

## Decision

Use **Freqtrade** as Testing Engine v1.

Use **NautilusTrader** later as a second, stricter test for strategies that pass Freqtrade.

Do not use LEAN or VectorBT as the main engine now.

## Why Freqtrade is best for this project now

- Built for crypto spot and futures.
- Python strategies. The Adapter can generate Python code for it.
- One tool supports backtest, parameter search, look-ahead checks, recursive checks, dry-run, and later live trading.
- Free and open source.
- It has a clear strategy interface, so the Adapter can always create the same type of runnable file.

Sources: [Freqtrade repository](https://github.com/freqtrade/freqtrade), [strategy guide](https://www.freqtrade.io/en/stable/strategy-101/), [look-ahead checks](https://docs.freqtrade.io/en/stable/lookahead-analysis/), [parameter search](https://www.freqtrade.io/en/stable/hyperopt/).

## What the Adapter must output

Every accepted Adapter result must create:

```text
testing_engine/strategies/StrategyName.py
testing_engine/configs/StrategyName.json
testing_engine/source_notes/StrategyName.md
```

- `StrategyName.py`: Freqtrade `IStrategy` Python class.
- Config: pairs, timeframe, fees, starting balance, position limits.
- Source notes: original link and every changed rule.
- No `unknown` fields. If a rule is missing, reject the source.

## Required test flow

```text
Code loads
→ historical backtest with fees
→ look-ahead check
→ recursive check
→ limited parameter search on old data only
→ hidden newer-data test
→ dry-run with live data
```

- Use Freqtrade `backtesting` for historical runs.
- Use `lookahead-analysis` and `recursive-analysis` before accepting results.
- Use `hyperopt` only after the base strategy works. Save every tried setting.
- Use `dry_run: true` before any real money. Freqtrade warns that dry-run is more reliable than backtesting alone. [Docs](https://www.freqtrade.io/en/stable/strategy-101/)

## Why not the other tools now

| Tool | Decision | Reason |
| --- | --- | --- |
| Freqtrade | Use now | Best crypto-first path from generated Python strategy to test and dry-run. |
| NautilusTrader | Use later | Better execution realism, order-book data, latency, and fill models; more setup. [Docs](https://nautilustrader.io/docs/latest/concepts/backtesting/) |
| LEAN | Not now | Strong multi-asset engine, but more complex and its local tooling has paid-tier limits. [Docs](https://www.quantconnect.com/docs/v2/lean-cli/backtesting/deployment) |
| VectorBT | Optional quick screen | Very fast for testing many settings, but not the main execution test or live path. Its community edition uses a Fair Code license. [Repository](https://github.com/polakowo/vectorbt) |

## Important limit

Freqtrade backtests assume orders fill. Passing a backtest is not proof a strategy works.

Later, repeat only the best strategies in NautilusTrader with worse fills, slippage, and latency. NautilusTrader supports deterministic event-driven backtests and configurable fill models. [Docs](https://nautilustrader.io/docs/latest/concepts/backtesting/)
