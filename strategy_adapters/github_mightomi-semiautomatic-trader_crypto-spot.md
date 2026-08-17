# Strategy adapter: mightomi

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/mightomi/SemiAutomatic-Trader
- Source market: `crypto`
- Author: mightomi
- Summary: A GUI based programmable stock/crypto trading interface to practice trading/swing-trading with virtual money.

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

- Result: Claude reviewed the public source; proposed breakout rules: EMA 16/44, RSI entry > 54, exit < 47, stop-loss -8%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
