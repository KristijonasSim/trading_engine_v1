# Strategy adapter: Evaluation of Dynamic Cointegration-Based Pairs Trading Strategy in the Cryptocurrency Market

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/2109.10662v1
- Source market: `crypto`
- Author: Masood Tadi, Irina Kortchmeski
- Summary: This research aims to demonstrate a dynamic cointegration-based pairs trading strategy, including an optimal look-back window framework in the cryptocurrency market, and evaluate its return and risk by applying three different scenarios. We employ the Engle-Granger methodology, the Kapetanios-Snell-Shin (KSS) test, and the Johansen test as cointegration tests in different scenarios. We calibrate the mean-reversion speed of the Ornstein-Uhlenbeck process to obtain the half-life used for the asset selection phase and look-back window estimation. By considering the main limitations in the market microstructure, our strategy exceeds the naive buy-and-hold approach in the Bitmex exchange. Another significant finding is that we implement a numerous collection of cryptocurrency coins to formulate the model's spread, which improves the risk-adjusted profitability of the pairs trading strategy. Besides, the strategy's maximum drawdown level is reasonably low, which makes it useful to be deployed. The results also indicate that a class of coins has better potential arbitrage opportunities than others. This research has some noticeable advantages, making it stand out from similar studies in the cryptocurrency market. First is the accuracy of data in which minute-binned data create the signals in the formation period. Besides, to backtest the strategy during the trading period, we simulate the trading signals using best bid/ask quotes and market trades. We exclusively take the order execution into account when the asset size is already available at its quoted price (with one or more period gaps after signal generation). This action makes the backtesting much more realistic.

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

- Result: Claude reviewed the public source; proposed mean_reversion rules: EMA 4/57, RSI entry > 30, exit < 48, stop-loss -3%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
