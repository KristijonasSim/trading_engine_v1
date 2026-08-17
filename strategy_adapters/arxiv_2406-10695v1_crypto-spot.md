# Strategy adapter: Statistical arbitrage in multi-pair trading strategy based on graph clustering algorithms in US equities market

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/2406.10695v1
- Source market: `general`
- Author: Adam Korniejczuk, Robert Ślepaczuk
- Summary: The study seeks to develop an effective strategy based on the novel framework of statistical arbitrage based on graph clustering algorithms. Amalgamation of quantitative and machine learning methods, including the Kelly criterion, and an ensemble of machine learning classifiers have been used to improve risk-adjusted returns and increase immunity to transaction costs over existing approaches. The study seeks to provide an integrated approach to optimal signal detection and risk management. As a part of this approach, innovative ways of optimizing take profit and stop loss functions for daily frequency trading strategies have been proposed and tested. All of the tested approaches outperformed appropriate benchmarks. The best combinations of the techniques and parameters demonstrated significantly better performance metrics than the relevant benchmarks. The results have been obtained under the assumption of realistic transaction costs, but are sensitive to changes in some key parameters.

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

- Result: Claude reviewed the public source; proposed mean_reversion rules: EMA 6/28, RSI entry > 30, exit < 58, stop-loss -5%, fixed $100 position, 1d. Testing must judge it; it is not claimed as the original author's exact strategy.
