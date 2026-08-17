# Strategy adapter: Trading Strategies of a Leveraged ETF in a Continuous Double Auction Market Using an Agent-Based Simulation

## Status

- Status: `ai_hypothesis`
- Target: `crypto-futures`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/2010.13036v1
- Source market: `futures`
- Author: Isao Yagi, Shunya Maruyama, Takanobu Mizuta
- Summary: A leveraged ETF is a fund aimed at achieving a rate of return several times greater than that of the underlying asset such as Nikkei 225 futures. Recently, it has been suggested that rebalancing trades of a leveraged ETF may destabilize the financial markets. An empirical study using an agent-based simulation indicated that a rebalancing trade strategy could affect the price formation of an underlying asset market. However, no leveraged ETF trading method for suppressing the increase in volatility as much as possible has yet been proposed. In this paper, we compare different strategies of trading for a proposed trading model and report the results of our investigation regarding how best to suppress an increase in market volatility. As a result, it was found that as the minimum number of orders in a rebalancing trade increases, the impact on the market price formation decreases.

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

- Result: Claude reviewed the public source; proposed volatility_regime rules: EMA 10/52, RSI entry > 51, exit < 46, stop-loss -5%, fixed $100 position, 1d. Testing must judge it; it is not claimed as the original author's exact strategy.
