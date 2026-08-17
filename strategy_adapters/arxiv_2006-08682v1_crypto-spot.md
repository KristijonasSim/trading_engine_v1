# Strategy adapter: The Importance of Low Latency to Order Book Imbalance Trading Strategies

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/2006.08682v1
- Source market: `stocks`
- Author: David Byrd, Sruthi Palaparthi, Maria Hybinette, Tucker Hybinette Balch
- Summary: There is a pervasive assumption that low latency access to an exchange is a key factor in the profitability of many high-frequency trading strategies. This belief is evidenced by the "arms race" undertaken by certain financial firms to co-locate with exchange servers. To the best of our knowledge, our study is the first to validate and quantify this assumption in a continuous double auction market with a single exchange similar to the New York Stock Exchange. It is not feasible to conduct this exploration with historical data in which trader identity and location are not reported. Accordingly, we investigate the relationship between latency of access to order book information and profitability of trading strategies exploiting that information with an agent-based interactive discrete event simulation in which thousands of agents pursue archetypal trading strategies. We introduce experimental traders pursuing a low-latency order book imbalance (OBI) strategy in a controlled manner across thousands of simulated trading days, and analyze OBI trader profit while varying distance (latency) from the exchange. Our experiments support that latency is inversely related to profit for the OBI traders, but more interestingly show that latency rank, rather than absolute magnitude, is the key factor in allocating returns among agents pursuing a similar strategy.

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

- Result: Claude reviewed the public source; proposed trend_strength rules: EMA 15/23, RSI entry > 63, exit < 35, stop-loss -9%, fixed $100 position, 5m. Testing must judge it; it is not claimed as the original author's exact strategy.
