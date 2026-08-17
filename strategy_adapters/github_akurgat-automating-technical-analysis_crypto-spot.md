# Strategy adapter: akurgat

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/akurgat/automating-technical-analysis
- Source market: `general`
- Author: akurgat
- Summary: Using data analytics alongside popular trading strategies and indicators, to identify best trading actions based solely on the price action.

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

- Result: Claude reviewed the public source; proposed mean_reversion rules: EMA 9/59, RSI entry > 28, exit < 55, stop-loss -8%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
