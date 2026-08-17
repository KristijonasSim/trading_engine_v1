# Strategy adapter: alpacahq

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/alpacahq/example-scalping
- Source market: `stocks`
- Author: alpacahq
- Summary: A working example algorithm for scalping strategy trading multiple stocks concurrently using python asyncio

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

- Result: Claude reviewed the public source; proposed trend_strength rules: EMA 3/43, RSI entry > 55, exit < 49, stop-loss -9%, fixed $100 position, 5m. Testing must judge it; it is not claimed as the original author's exact strategy.
