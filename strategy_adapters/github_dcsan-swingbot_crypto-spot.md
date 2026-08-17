# Strategy adapter: dcsan

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/dcsan/swingbot
- Source market: `crypto`
- Author: dcsan
- Summary: Crypto Trading simulator with simple Swing strategies

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

- Result: Claude reviewed the public source; proposed mean_reversion rules: EMA 18/31, RSI entry > 34, exit < 49, stop-loss -5%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
