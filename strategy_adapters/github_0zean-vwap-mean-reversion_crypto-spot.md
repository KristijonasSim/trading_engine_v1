# Strategy adapter: 0zean Mean Reversion

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/0zean/VWAP-Mean-Reversion
- Source market: `general`
- Author: 0zean
- Summary: A VWAP based mean reversion trading strategy

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

- Result: Claude reviewed the public source; proposed mean_reversion rules: EMA 11/24, RSI entry > 42, exit < 50, stop-loss -3%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
