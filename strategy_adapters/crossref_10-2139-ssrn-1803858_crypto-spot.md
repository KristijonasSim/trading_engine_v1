# Strategy adapter: Mean Variance Optimal VWAP Trading

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://doi.org/10.2139/ssrn.1803858
- Source market: `stocks`
- Author: James McCulloch, Vlad Kazakov
- Summary: VWAP is the Volume Weighted Average Price of traded stock over a defined period. It is a metric of trade execution quality used by institutional traders to minimize the execution cost of large trades. A riskless VWAP trading strategy is not possible without knowledge of final market volume. We formulate a mean-variance optimal VWAP strategy by assuming knowledge of final volume and then project this onto the space of strategies accessible to the VWAP trader. The mean variance optimal VWAP trading strategy is the sum of two distinct trading strategies, a minimum variance VWAP hedging strategy and a `directional' price strategy independent of the hedging strategy and market VWAP. It is optimal for large volume VWAP traders to increase the size of the price `directional' trade for additional return.

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

- Result: Source page could not be read; proposed volatility_regime rules: EMA 17/33, RSI entry > 51, exit < 44, stop-loss -9%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
