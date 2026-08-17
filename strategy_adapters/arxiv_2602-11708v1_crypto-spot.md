# Strategy adapter: Crypto Time-Series Momentum

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/2602.11708v1
- Source market: `crypto`
- Author: Duc Bui, Thanh Nguyen
- Summary: Cryptocurrency markets exhibit pronounced momentum effects and regime-dependent volatility, presenting both opportunities and challenges for systematic trading strategies. We propose AdaptiveTrend, a multi-component algorithmic trading framework that integrates high-frequency trend-following on 6-hour intervals with monthly adaptive portfolio construction and asymmetric long-short capital allocation. Our framework introduces three key innovations: (1) a dynamic trailing stop mechanism calibrated to intra-day volatility regimes, (2) a rolling Sharpe-ratio-based asset selection procedure with market-capitalization-aware filtering, and (3) a theoretically motivated asymmetric 70/30 long-short allocation scheme grounded in the empirical positive drift of crypto markets. Through extensive out-of-sample backtesting across 150+ cryptocurrency pairs over a 36-month evaluation window (2022-2024), AdaptiveTrend achieves an annualized Sharpe ratio of 2.41, a maximum drawdown of -12.7%, and a Calmar ratio of 3.18, significantly outperforming benchmark trend-following strategies (TSMOM, time-series momentum) and equal-weighted buy-and-hold portfolios. We further conduct rigorous robustness analyses including parameter sensitivity, transaction cost modeling, and regime-conditional performance decomposition, demonstrating the strategy's resilience across bull, bear, and sideways market conditions.

## Original rules

- Entry: 6-hour trend-following signal; exact indicator and threshold are not stated.
- Exit: Exit when the trend signal ends; exact rule is not stated.
- Stop loss: Dynamic trailing stop based on intraday volatility; exact formula is not stated.
- Position size: Original source uses asymmetric 70/30 long/short allocation.

## Crypto adaptation

- Pairs: Start with liquid majors only; exact list must be fixed before testing.
- Timeframe: `6h`.
- Session or UTC time: Continuous 24/7 market; use UTC candles.
- Long / short rule: Spot adaptation is long/cash only. Replace the source's short allocation with cash.
- Fee and slippage: `unknown`
- What changed from original: Removed short positions because this is crypto spot. The exact trend indicator, trailing-stop formula, universe, fees, and position weights remain unknown.

## Approval

- Reviewer:
- Decision: `needs work`
- Ready for Testing Engine: `no`

## Automation

- Result: Skipped automatically: entry, exit, stop-loss, or position-size rules are not complete enough to create honest test code.
