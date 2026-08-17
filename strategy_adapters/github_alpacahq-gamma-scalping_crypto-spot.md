# Strategy adapter: alpacahq

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/alpacahq/gamma-scalping
- Source market: `general`
- Author: alpacahq
- Summary: Runnable algo template for gamma scalping options trading strategy

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

- Result: Claude reviewed the public source; proposed volatility_regime rules: EMA 17/29, RSI entry > 60, exit < 52, stop-loss -9%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
