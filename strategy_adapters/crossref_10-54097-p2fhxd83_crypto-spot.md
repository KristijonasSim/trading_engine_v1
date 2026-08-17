# Strategy adapter: Comparison of Cross-sectional Momentum Strategy and Time-Series Momentum Strategy

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://doi.org/10.54097/p2fhxd83
- Source market: `stocks`
- Author: Wei Chen
- Summary: There are all kinds of quantitative portfolios used in the stock investing such as momentum, mean reversion, liquidity and so on. Cross-sectional momentum and Time-series momentum are the two main method of momentum strategies. They are also the basic methods that were used to construct the portfolio of investing. The essay analyses the difference of the theoretical definition and compares the two methods’ return, sharp ratio, maximum drawdown and some other indicators in a relative stable and prosperous environment which is simulated by well performed stocks in the 10 years’ period without considering the transaction cost. The result finds that the time-series momentum and cross-sectional momentum both generate positive return in the environment that is simulated. Moreover, the time-series momentum even performs better than cross-sectional momentum strategies in the stable and prosperous environment. The essay also points out the limitation of the experiment and presents some useful advice for the investors who want to invest in the stock market.

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

- Result: Claude reviewed the public source; proposed trend_strength rules: EMA 4/29, RSI entry > 51, exit < 49, stop-loss -10%, fixed $100 position, 1d. Testing must judge it; it is not claimed as the original author's exact strategy.
