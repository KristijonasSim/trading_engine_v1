# Strategy adapter: Arthur-plg

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/Arthur-plg/crypto-swing-bot
- Source market: `crypto`
- Author: Arthur-plg
- Summary: A Python-based backtesting engine and swing trading bot designed to capture cryptocurrency volatility using a conservative mean-reversion strategy on a 4-hour timeframe.

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

- Result: Claude reviewed the public source; proposed mean_reversion rules: EMA 10/55, RSI entry > 32, exit < 61, stop-loss -2%, fixed $100 position, 4h. Testing must judge it; it is not claimed as the original author's exact strategy.
