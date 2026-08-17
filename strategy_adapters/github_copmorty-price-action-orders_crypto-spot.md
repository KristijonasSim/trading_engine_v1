# Strategy adapter: copmorty

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/copmorty/price_action_orders
- Source market: `crypto`
- Author: copmorty
- Summary: Flutter desktop app for trading cryptocurrencies on Binance.

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

- Result: Claude reviewed the public source; proposed breakout rules: EMA 12/45, RSI entry > 55, exit < 48, stop-loss -8%, fixed $100 position, 4h. Testing must judge it; it is not claimed as the original author's exact strategy.
