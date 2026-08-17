# Strategy adapter: LeviathanLevi Momentum

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/LeviathanLevi/BinanceUS-Crypto-Trading-Bot
- Source market: `crypto`
- Author: LeviathanLevi
- Summary: Binance.US crypto trading bot. Implemented with Python, python-binance library, and the Binance.US API. Uses a configurable momentum trading strategy.

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

- Result: Claude reviewed the public source; proposed trend_strength rules: EMA 12/54, RSI entry > 55, exit < 43, stop-loss -7%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
