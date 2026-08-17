# Strategy adapter: Optimal Limit-versus-Market Order Slicing Under a VWAP Benchmark - Continuous Case

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://doi.org/10.2139/ssrn.2318896
- Source market: `stocks`
- Author: Tianhui Li
- Summary: Algorithmic brokers benchmarked to TWAP or VWAP face a limit-order market-order tradeoff when slicing orders. Executing market orders keeps them on schedule but is costly. Executing limit orders saves spread but can lead to schedule slippage. We build on our results in the discrete shares case Li [2012] to present an optimal solution for execution in light of this tradeoff in the limit of continuous shares. As in the discrete case, the optimal solution is described in terms of a forward and backward boundary which define how many limit orders should be placed on the order book and when to execute market orders. Closed-form solutions for the boundaries are derived for the “stationary limit.” These boundaries can be computed numerically in the general case.

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

- Result: Source page could not be read; proposed volatility_regime rules: EMA 13/51, RSI entry > 55, exit < 39, stop-loss -8%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
