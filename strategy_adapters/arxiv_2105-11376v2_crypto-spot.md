# Strategy adapter: Can we imitate the principal investor's behavior to learn option price?

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/2105.11376v2
- Source market: `stocks`
- Author: Xin Jin
- Summary: This paper presents a framework of imitating the principal investor's behavior for optimal pricing and hedging options. We construct a non-deterministic Markov decision process for modeling stock price change driven by the principal investor's decision making. However, low signal-to-noise ratio and instability that are inherent in equity markets pose challenges to determine the state transition (stock price change) after executing an action (the principal investor's decision) as well as decide an action based on current state (spot price). In order to conquer these challenges, we resort to a Bayesian deep neural network for computing the predictive distribution of the state transition led by an action. Additionally, instead of exploring a state-action relationship to formulate a policy, we seek for an episode based visible-hidden state-action relationship to probabilistically imitate the principal investor's successive decision making. Unlike conventional option pricing that employs analytical stochastic processes or utilizes time series analysis to model and sample underlying stock price movements, our algorithm simulates stock price paths by imitating the principal investor's behavior which requires no preset probability distribution and fewer predetermined parameters. Eventually the optimal option price is learned by reinforcement learning to maximize the cumulative risk-adjusted return of a dynamically hedged portfolio over simulated price paths.

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

- Result: Claude reviewed the public source; proposed volatility_regime rules: EMA 13/49, RSI entry > 61, exit < 46, stop-loss -5%, fixed $100 position, 4h. Testing must judge it; it is not claimed as the original author's exact strategy.
