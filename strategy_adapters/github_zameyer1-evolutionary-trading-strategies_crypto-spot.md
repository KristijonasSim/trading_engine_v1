# Strategy adapter: zameyer1

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/zameyer1/Evolutionary-Trading-Strategies
- Source market: `stocks`
- Author: zameyer1
- Summary: This code illustrates the use of genetic programming to evolve financial trading strategies for a single equity stock. Individuals (strategies) are considered as functions of historical price data, outputting a position allocation. Strategy fitness evaluation is computed by simulating the strategy over historical financial data. Because financial investment requires a fundamental tradeoff between risk and return, strategies are evaluated on multi-objective fitness functions depending on profit and maximum drawdown of the strategy and ranging from very risk-prone to very risk-averse. The population of individual strategies is evolved using tournament selection, single-point crossover, and random mutation as evolutionary operators. Strategies with the best fitness at any stage in the evolutionary process are recorded in a ‘hall-of-fame’. At the end of the evolutionary process, strategies in the ‘hall-of-fame’ are evaluated over a set of test data and selected based on a train-test criterion which penalizes strategies that do not generalize well.

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

- Result: Source page could not be read; proposed breakout rules: EMA 16/24, RSI entry > 52, exit < 51, stop-loss -4%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
