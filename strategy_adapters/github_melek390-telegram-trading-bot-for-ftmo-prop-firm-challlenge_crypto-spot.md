# Strategy adapter: Melek390 Momentum

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/Melek390/Telegram-trading-bot-for-FTMO-prop-firm-challlenge
- Source market: `general`
- Author: Melek390
- Summary: Automated Telegram-controlled trading bot for FTMO prop-firm challenges. Runs three uncorrelated, honestly-validated strategies (VWAP pullback, IBS mean-reversion, Donchian momentum) live on the cTrader Open API walk-forward tested with realistic costs and fill-rate audits.

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

- Result: Claude reviewed the public source; proposed breakout rules: EMA 8/45, RSI entry > 60, exit < 46, stop-loss -9%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
