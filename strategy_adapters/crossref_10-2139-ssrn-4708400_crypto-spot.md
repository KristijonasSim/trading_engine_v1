# Strategy adapter: Efficacy of a Mean Reversion Trading Strategy Using True Strength Index

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://doi.org/10.2139/ssrn.4708400
- Source market: `stocks`
- Author: Daniel Requejo
- Summary: This paper presents a comprehensive analysis of a mean reversion trading strategy, centered around the True Strength Index (TSI), applied to the SPY (S&amp;P 500) and QQQ (Nasdaq Index) ETFs. The study spans historical data from 1996 to 2022, encompassing various market conditions to assess the strategy's robustness. The core methodology involves generating open and close signals based on the TSI, with supplementary insights from the Relative Strength Index (RSI) and other technical indicators.<br><br>Through rigorous backtesting, the paper evaluates key performance metrics such as Compound Annual Growth Rate (CAGR), Maximum Drawdown (Max DD), Sharpe Ratio, and Sortino Ratio. These metrics illuminate the strategy's profitability, risk management efficiency, and overall effectiveness. The strategy's adaptability is further demonstrated through a detailed walk-forward analysis, highlighting its performance over sequential three-year periods.<br><br>The paper aims to contribute to the financial market trading strategies literature, offering a nuanced understanding of the applicability and sustainability of mean reversion approaches in the dynamic landscape of equity markets. It offers a balanced view, discussing the strategy’s strengths, limitations, and broader implications for investors and traders. This research is significant for those seeking systematic methods to navigate the complexities of financial trading, underlining the importance of continuous adaptation and risk-awareness in investment practices.

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

- Result: Source page could not be read; proposed mean_reversion rules: EMA 5/34, RSI entry > 33, exit < 49, stop-loss -6%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
