# Strategy adapter: The microscopic relationships between triangular arbitrage and cross-currency correlations in a simple agent based model of foreign exchange markets

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/2002.02583v1
- Source market: `forex`
- Author: Alberto Ciacci, Takumi Sueshige, Hideki Takayasu, Kim Christensen, Misako Takayasu
- Summary: Foreign exchange rates movements exhibit significant cross-correlations even on very short time-scales. The effect of these statistical relationships become evident during extreme market events, such as flash crashes.In this scenario, an abrupt price swing occurring on a given market is immediately followed by anomalous movements in several related foreign exchange rates. Although a deep understanding of cross-currency correlations would be clearly beneficial for conceiving more stable and safer foreign exchange markets, the microscopic origins of these interdependencies have not been extensively investigated. We introduce an agent-based model which describes the emergence of cross-currency correlations from the interactions between market makers and an arbitrager. Our model qualitatively replicates the time-scale vs. cross-correlation diagrams observed in real trading data, suggesting that triangular arbitrage plays a primary role in the entanglement of the dynamics of different foreign exchange rates. Furthermore, the model shows how the features of the cross-correlation function between two foreign exchange rates, such as its sign and value, emerge from the interplay between triangular arbitrage and trend-following strategies.

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

- Result: Claude reviewed the public source; proposed trend_strength rules: EMA 7/22, RSI entry > 61, exit < 41, stop-loss -5%, fixed $100 position, 15m. Testing must judge it; it is not claimed as the original author's exact strategy.
