# Strategy adapter: Evaluating the Performance of a Donchian Channel Breakout Strategy with ATR-Based Risk Management

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://doi.org/10.2139/ssrn.6272239
- Source market: `crypto`
- Author: Nitish Poluri
- Summary: This study examines the performance of the Donchian Channel breakout strategy enhanced with the ATR-based volatility regime filter and ATR based risk management. Using BTC (Bitcoin) daily data, the strategy enters long and short positions on range breakouts while restricting high volatility trades. Backtesting results indicate that the strategy significantly outperformed a passive based approach over the tested period, however these results were very specific and narrow and were highly sensitive to transactional costs, parameter settings, and market conditions. The findings highlight the importance of volatility filtering and risk controls in trendy systems that follow crypto markets.

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

- Result: Source page could not be read; proposed breakout_momentum rules: EMA 13/37, RSI entry > 59, exit < 43, stop-loss -6%, fixed $100 position, 1d. Testing must judge it; it is not claimed as the original author's exact strategy.
