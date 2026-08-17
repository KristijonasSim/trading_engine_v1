# Strategy adapter: quantrocket-codeload

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/quantrocket-codeload/pairs-pipeline
- Source market: `general`
- Author: quantrocket-codeload
- Summary: Pairs trading strategy that includes a research pipeline for identifying and selecting pairs. Tests all possible pairs in a universe for cointegration using the Johansen test, then runs in-sample backtests on all cointegrating pairs, then runs an out-of-sample backtest on the 5 best performing pairs.

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

- Result: Source page could not be read; proposed volatility_regime rules: EMA 11/59, RSI entry > 46, exit < 50, stop-loss -8%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
