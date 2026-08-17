# Strategy adapter: DDPG based on multi-scale strokes for financial time series trading strategy

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/2207.10071v1
- Source market: `stocks`
- Author: Jun-Cheng Chen, Cong-Xiao Chen, Li-Juan Duan, Zhi Cai
- Summary: With the development of artificial intelligence,more and more financial practitioners apply deep reinforcement learning to financial trading strategies.However,It is difficult to extract accurate features due to the characteristics of considerable noise,highly non-stationary,and non-linearity of single-scale time series,which makes it hard to obtain high returns.In this paper,we extract a multi-scale feature matrix on multiple time scales of financial time series,according to the classic financial theory-Chan Theory,and put forward to an approach of multi-scale stroke deep deterministic policy gradient reinforcement learning model(MSSDDPG)to search for the optimal trading strategy.We carried out experiments on the datasets of the Dow Jones,S&P 500 of U.S. stocks, and China's CSI 300,SSE Composite,evaluate the performance of our approach compared with turtle trading strategy, Deep Q-learning(DQN)reinforcement learning strategy,and deep deterministic policy gradient (DDPG) reinforcement learning strategy.The result shows that our approach gets the best performance in China CSI 300,SSE Composite,and get an outstanding result in Dow Jones,S&P 500 of U.S.

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

- Result: Claude reviewed the public source; proposed trend_strength rules: EMA 6/22, RSI entry > 54, exit < 41, stop-loss -10%, fixed $100 position, 1d. Testing must judge it; it is not claimed as the original author's exact strategy.
