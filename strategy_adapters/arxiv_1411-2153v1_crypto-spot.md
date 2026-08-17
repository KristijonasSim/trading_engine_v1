# Strategy adapter: Evolving intraday foreign exchange trading strategies utilizing multiple instruments price series

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/1411.2153v1
- Source market: `forex`
- Author: Simone Cirillo, Stefan Lloyd, Peter Nordin
- Summary: We propose a Genetic Programming architecture for the generation of foreign exchange trading strategies. The system's principal features are the evolution of free-form strategies which do not rely on any prior models and the utilization of price series from multiple instruments as input data. This latter feature constitutes an innovation with respect to previous works documented in literature. In this article we utilize Open, High, Low, Close bar data at a 5 minutes frequency for the AUD.USD, EUR.USD, GBP.USD and USD.JPY currency pairs. We will test the implementation analyzing the in-sample and out-of-sample performance of strategies for trading the USD.JPY obtained across multiple algorithm runs. We will also evaluate the differences between strategies selected according to two different criteria: one relies on the fitness obtained on the training set only, the second one makes use of an additional validation dataset. Strategy activity and trade accuracy are remarkably stable between in and out of sample results. From a profitability aspect, the two criteria both result in strategies successful on out-of-sample data but exhibiting different characteristics. The overall best performing out-of-sample strategy achieves a yearly return of 19%.

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

- Result: Claude reviewed the public source; proposed trend_strength rules: EMA 11/26, RSI entry > 65, exit < 40, stop-loss -9%, fixed $100 position, 5m. Testing must judge it; it is not claimed as the original author's exact strategy.
