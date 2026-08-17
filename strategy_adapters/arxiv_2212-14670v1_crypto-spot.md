# Strategy adapter: Hierarchical Deep Reinforcement Learning for VWAP Strategy Optimization

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/2212.14670v1
- Source market: `stocks`
- Author: Xiaodong Li, Pangjing Wu, Chenxin Zou, Qing Li
- Summary: Designing an intelligent volume-weighted average price (VWAP) strategy is a critical concern for brokers, since traditional rule-based strategies are relatively static that cannot achieve a lower transaction cost in a dynamic market. Many studies have tried to minimize the cost via reinforcement learning, but there are bottlenecks in improvement, especially for long-duration strategies such as the VWAP strategy. To address this issue, we propose a deep learning and hierarchical reinforcement learning jointed architecture termed Macro-Meta-Micro Trader (M3T) to capture market patterns and execute orders from different temporal scales. The Macro Trader first allocates a parent order into tranches based on volume profiles as the traditional VWAP strategy does, but a long short-term memory neural network is used to improve the forecasting accuracy. Then the Meta Trader selects a short-term subgoal appropriate to instant liquidity within each tranche to form a mini-tranche. The Micro Trader consequently extracts the instant market state and fulfils the subgoal with the lowest transaction cost. Our experiments over stocks listed on the Shanghai stock exchange demonstrate that our approach outperforms baselines in terms of VWAP slippage, with an average cost saving of 1.16 base points compared to the optimal baseline.

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

- Result: Claude reviewed the public source; proposed mean_reversion rules: EMA 13/23, RSI entry > 32, exit < 60, stop-loss -5%, fixed $100 position, 15m. Testing must judge it; it is not claimed as the original author's exact strategy.
