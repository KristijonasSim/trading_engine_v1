# Strategy adapter: VWAP-Based Regime Classification Model for Intraday Price Dynamics

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://doi.org/10.2139/ssrn.6438039
- Source market: `general`
- Author: Chong Yul Lee
- Summary: This paper introduces a quantitative framework for classifying intraday market regimes using deviations from the Volume Weighted Average Price (VWAP). By normalizing price deviations relative to VWAP with a volatility-adjusted metric, the model distinguishes between trend-dominated and mean-reverting environments. A regime variable is defined based on threshold conditions, allowing for systematic identification of directional bias and market structure. The proposed model provides a mathematically grounded interpretation of widely used trading heuristics and offers a bridge between technical analysis and market microstructure theory.

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

- Result: Source page could not be read; proposed volatility_regime rules: EMA 18/64, RSI entry > 54, exit < 53, stop-loss -4%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
