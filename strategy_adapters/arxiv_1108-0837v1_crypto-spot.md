# Strategy adapter: Constructing the Best Trading Strategy: A New General Framework

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/1108.0837v1
- Source market: `general`
- Author: Philip Z. Maymin, Zakhar G. Maymin
- Summary: We introduce a new general framework for constructing the best trading strategy for a given historical indicator. We construct the unique trading strategy with the highest expected return. This optimal strategy may be implemented directly, or its expected return may be used as a benchmark to evaluate how far away from the optimal other proposed strategies for the given indicators are. Separately, we also construct the unique trading strategy with the highest information ratio. In the normal case, when the traded security return is near zero, and for reasonable correlations, the performance differences are economically insignificant. However, when the correlation approaches one, the trading strategy with the highest expected return approaches its maximum information ratio of 1.32 while the trading strategy with the highest information ratio goes to infinity.

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

- Result: Claude reviewed the public source; proposed trend_strength rules: EMA 12/41, RSI entry > 59, exit < 43, stop-loss -5%, fixed $100 position, 1d. Testing must judge it; it is not claimed as the original author's exact strategy.
