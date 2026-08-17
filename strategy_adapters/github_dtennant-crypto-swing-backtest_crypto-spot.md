# Strategy adapter: DTennant

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/DTennant/crypto-swing-backtest
- Source market: `crypto`
- Author: DTennant
- Summary: Crypto swing trading strategy backtest framework — pure Python, zero dependencies. 9 strategies × 5 coins.

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

- Result: Claude reviewed the public source; proposed mean_reversion rules: EMA 20/59, RSI entry > 39, exit < 49, stop-loss -2%, fixed $100 position, 1d. Testing must judge it; it is not claimed as the original author's exact strategy.
