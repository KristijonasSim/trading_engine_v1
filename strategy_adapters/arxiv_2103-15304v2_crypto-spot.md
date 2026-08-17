# Strategy adapter: A Comparative Evaluation of Predominant Deep Learning Quantified Stock Trading Strategies

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/2103.15304v2
- Source market: `stocks`
- Author: Haohan Zhang
- Summary: This study first reconstructs three deep learning powered stock trading models and their associated strategies that are representative of distinct approaches to the problem and established upon different aspects of the many theories evolved around deep learning. It then seeks to compare the performance of these strategies from different perspectives through trading simulations ran on three scenarios when the benchmarks are kept at historical low points for extended periods of time. The results show that in extremely adverse market climates, investment portfolios managed by deep learning powered algorithms are able to avert accumulated losses by generating return sequences that shift the constantly negative CSI 300 benchmark return upward. Among the three, the LSTM model's strategy yields the best performance when the benchmark sustains continued loss.

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

- Result: Claude reviewed the public source; proposed trend_strength rules: EMA 9/20, RSI entry > 52, exit < 41, stop-loss -9%, fixed $100 position, 1d. Testing must judge it; it is not claimed as the original author's exact strategy.
