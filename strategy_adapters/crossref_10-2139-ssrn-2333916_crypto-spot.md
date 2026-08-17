# Strategy adapter: Optimal VWAP Tracking

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://doi.org/10.2139/ssrn.2333916
- Source market: `stocks`
- Author: Daniel Mitchell, Jedrzej Pawel Bialkowski, Stathis Tompaidis
- Summary: We consider the problem of finding a strategy that tracks the volume weighted average price (VWAP) of a stock, a key measure of execution quality for large orders used by institutional investors. We obtain the optimal, dynamic, VWAP tracking strategy in closed form in a model with general price and volume dynamics and show that it can be extended to incorporate proportional transaction costs. We build a model of intraday volume using the Trade and Quote dataset to empirically test the strategy, both without trading costs and when trading has temporary effects that include the bid-ask spread and depth of the order book, and permanent effects that reflect the potential information content of trades. We find that the implementation cost of the strategy we propose is lower than the cost charged by brokerage houses.

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

- Result: Source page could not be read; proposed breakout_momentum rules: EMA 3/37, RSI entry > 62, exit < 41, stop-loss -8%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
