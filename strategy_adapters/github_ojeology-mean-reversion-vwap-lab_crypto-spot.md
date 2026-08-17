# Strategy adapter: ojeology

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/ojeology/mean-reversion-vwap-lab
- Source market: `crypto`
- Author: ojeology
- Summary: A VWAP ±2σ mean-reversion crypto strategy, developed across 14 documented experiments (E1–E14) with full walk-forward validation. Includes the complete research journal, strategy version history, backtest results, and a live paper-trading bot. PF 2.01, Sharpe 15.4, $3.61/day OOS across 13 pairs

## Original rules

- Entry: `unknown`
- Exit: `unknown`
- Stop loss: `unknown`
- Position size: `unknown`

## Crypto adaptation

- Pairs: `unknown`
- Timeframe: `unknown`
- Session or UTC time: `unknown`
- Long / short rule: `unknown`
- Fee and slippage: `unknown`
- What changed from original: `unknown`

## Approval

- Reviewer:
- Decision: `needs work`
- Ready for Testing Engine: `no`

## Automation

- Result: Source page could not be read; proposed volatility_regime rules: EMA 10/60, RSI entry > 53, exit < 46, stop-loss -10%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
