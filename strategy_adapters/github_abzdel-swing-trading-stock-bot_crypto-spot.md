# Strategy adapter: abzdel

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/abzdel/Swing-Trading-Stock-Bot
- Source market: `stocks`
- Author: abzdel
- Summary: A Python-based bot that uses the Alpaca API and swing trading principles to buy and sell securities.

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

- Result: Claude reviewed the public source; proposed mean_reversion rules: EMA 18/37, RSI entry > 37, exit < 52, stop-loss -3%, fixed $100 position, 1d. Testing must judge it; it is not claimed as the original author's exact strategy.
