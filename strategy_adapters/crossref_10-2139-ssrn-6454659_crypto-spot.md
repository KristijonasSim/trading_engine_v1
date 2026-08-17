# Strategy adapter: Momentum Exhaustion and Fair Value Reversion: An ADX-conditioned VWAP Strategy in FX Markets

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://doi.org/10.2139/ssrn.6454659
- Source market: `forex`
- Author: Amaanullah Bhatti
- Summary: This paper develops a regime-conditioned trading framework for foreign exchange markets that exploits intraday mean reversion toward a volume-weighted fair value benchmark under conditions of momentum exhaustion. Three dimensions are integrated: price location relative to previous-session extremes, deviation from the Volume Weighted Average Price (VWAP), and trend strength as measured by Wilder's Average Directional Index (ADX). The strategy generates short (long) signals when price reaches prior-session highs (lows) while simultaneously exhibiting large positive (negative) VWAP deviations and a turning-over ADX, which collectively indicate that directional momentum is fading. The model bridges market-microstructure theory-specifically the role of VWAP as an institutional benchmark price-with technical regime filtering, contributing a theoretically grounded, state-conditioned mean-reversion framework to the FX literature. Formal backtesting and performance attribution are left to future work.

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

- Result: Source page could not be read; proposed mean_reversion rules: EMA 8/28, RSI entry > 42, exit < 61, stop-loss -3%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
