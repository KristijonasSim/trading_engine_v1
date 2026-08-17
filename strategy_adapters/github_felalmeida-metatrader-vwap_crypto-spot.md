# Strategy adapter: felalmeida

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/felalmeida/Metatrader-vWap
- Source market: `stocks`
- Author: felalmeida
- Summary: VWAP is an intra-day calculation used primarily by algorithms and institutional traders to assess where a stock is trading relative to its volume weighted average for the day.

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

- Result: Claude reviewed the public source; proposed mean_reversion rules: EMA 6/30, RSI entry > 40, exit < 52, stop-loss -6%, fixed $100 position, 15m. Testing must judge it; it is not claimed as the original author's exact strategy.
