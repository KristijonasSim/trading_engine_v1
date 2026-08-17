# Strategy adapter: chj29

## Status

- Status: `ai_hypothesis`
- Target: `crypto-futures`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/chj29/personal-berkshire-trading-system
- Source market: `futures`
- Author: chj29
- Summary: VWAP Mean-Reversion Strategy for BTC Futures (Research Project)

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

- Result: Claude reviewed the public source; proposed mean_reversion rules: EMA 18/40, RSI entry > 33, exit < 57, stop-loss -4%, fixed $100 position, 5m. Testing must judge it; it is not claimed as the original author's exact strategy.
