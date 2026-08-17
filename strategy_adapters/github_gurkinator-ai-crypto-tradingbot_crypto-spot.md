# Strategy adapter: gurkinator

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/gurkinator/AI-Crypto-TradingBot
- Source market: `crypto`
- Author: gurkinator
- Summary: AI-driven KuCoin trading bot built with Python and Streamlit. Supports Swing/Day modes, background strategy scanning, Top 3 optimization, risk controls, Telegram alerts, KCS fee modeling, live position tracking and learning-based recommendations. Early beta, use at your own risk.

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

- Result: Claude reviewed the public source; proposed mean_reversion rules: EMA 5/48, RSI entry > 30, exit < 49, stop-loss -5%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
