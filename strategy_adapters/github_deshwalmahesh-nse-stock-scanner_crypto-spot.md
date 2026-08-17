# Strategy adapter: deshwalmahesh Momentum

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/deshwalmahesh/NSE-Stock-Scanner
- Source market: `stocks`
- Author: deshwalmahesh
- Summary: National Stock Exchange (NSE), India based Stock screener program. Supports Live Data, Swing / Momentum Trading, Intraday Trading, Connect to online brokers as Zerodha Kite, Risk Management, Emotion Control, Screening, Strategies, Backtesting, Automatic Stock Downloading after closing, live free day trading data and much more

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

- Result: Claude reviewed the public source; proposed trend_strength rules: EMA 11/52, RSI entry > 58, exit < 39, stop-loss -9%, fixed $100 position, 1d. Testing must judge it; it is not claimed as the original author's exact strategy.
