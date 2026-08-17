# Strategy adapter: Exploration of Algorithmic Trading Strategies for the Bitcoin Market

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/2110.14936v1
- Source market: `crypto`
- Author: Nathan Crone, Eoin Brophy, Tomas Ward
- Summary: Bitcoin is firmly becoming a mainstream asset in our global society. Its highly volatile nature has traders and speculators flooding into the market to take advantage of its significant price swings in the hope of making money. This work brings an algorithmic trading approach to the Bitcoin market to exploit the variability in its price on a day-to-day basis through the classification of its direction. Building on previous work, in this paper, we utilise both features internal to the Bitcoin network and external features to inform the prediction of various machine learning models. As an empirical test of our models, we evaluate them using a real-world trading strategy on completely unseen data collected throughout the first quarter of 2021. Using only a binary predictor, at the end of our three-month trading period, our models showed an average profit of 86\%, matching the results of the more traditional buy-and-hold strategy. However, after incorporating a risk tolerance score into our trading strategy by utilising the model's prediction confidence scores, our models were 12.5\% more profitable than the simple buy-and-hold strategy. These results indicate the credible potential that machine learning models have in extracting profit from the Bitcoin market and act as a front-runner for further research into real-world Bitcoin trading.

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

- Result: Claude reviewed the public source; proposed trend_strength rules: EMA 18/42, RSI entry > 57, exit < 43, stop-loss -5%, fixed $100 position, 1d. Testing must judge it; it is not claimed as the original author's exact strategy.
