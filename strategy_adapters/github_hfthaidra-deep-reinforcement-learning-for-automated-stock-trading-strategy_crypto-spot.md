# Strategy adapter: HFTHaidra

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/HFTHaidra/Deep-Reinforcement-Learning-for-Automated-Stock-Trading-Strategy
- Source market: `stocks`
- Author: HFTHaidra
- Summary: Stock trading strategies play a critical role in investment. However, it is challenging to design a profitable strategy in a complex and dynamic stock market. In this paper, we propose a deep ensemble reinforcement learning scheme that automatically learns a stock trading strategy by maximizing investment return. We train a deep reinforcement learning agent and obtain an ensemble trading strategy using the three actor-critic based algorithms: Proximal Policy Optimization (PPO), Advantage Actor Critic (A2C), and Deep Deterministic Policy Gradient (DDPG). The ensemble strategy inherits and integrates the best features of the three algorithms, thereby robustly adjusting to different market conditions. In order to avoid the large memory consumption in training networks with continuous action space, we employ a load-on-demand approach for processing very large data. We test our algorithms on the 30 Dow Jones stocks which have adequate liquidity. The performance of the trading agent with different reinforcement learning algorithms is evaluated and compared with both the Dow Jones Industrial Average index and the traditional min-variance portfolio allocation strategy. The proposed deep ensemble scheme is shown to outperform the three individual algorithms and the two baselines in terms of the risk-adjusted return measured by the Sharpe ratio.

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

- Result: Claude reviewed the public source; proposed volatility_regime rules: EMA 8/28, RSI entry > 51, exit < 43, stop-loss -4%, fixed $100 position, 1d. Testing must judge it; it is not claimed as the original author's exact strategy.
