# Strategy adapter: Deep Learning for VWAP Execution in Crypto Markets: Beyond the Volume Curve

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/2502.13722v2
- Source market: `crypto`
- Author: Remi Genet
- Summary: Volume-Weighted Average Price (VWAP) is arguably the most prevalent benchmark for trade execution as it provides an unbiased standard for comparing performance across market participants. However, achieving VWAP is inherently challenging due to its dependence on two dynamic factors, volumes and prices. Traditional approaches typically focus on forecasting the market's volume curve, an assumption that may hold true under steady conditions but becomes suboptimal in more volatile environments or markets such as cryptocurrency where prediction error margins are higher. In this study, I propose a deep learning framework that directly optimizes the VWAP execution objective by bypassing the intermediate step of volume curve prediction. Leveraging automatic differentiation and custom loss functions, my method calibrates order allocation to minimize VWAP slippage, thereby fully addressing the complexities of the execution problem. My results demonstrate that this direct optimization approach consistently achieves lower VWAP slippage compared to conventional methods, even when utilizing a naive linear model presented in arXiv:2410.21448. They validate the observation that strategies optimized for VWAP performance tend to diverge from accurate volume curve predictions and thus underscore the advantage of directly modeling the execution objective. This research contributes a more efficient and robust framework for VWAP execution in volatile markets, illustrating the potential of deep learning in complex financial systems where direct objective optimization is crucial. Although my empirical analysis focuses on cryptocurrency markets, the underlying principles of the framework are readily applicable to other asset classes such as equities.

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

- Result: Claude reviewed the public source; proposed mean_reversion rules: EMA 14/23, RSI entry > 36, exit < 62, stop-loss -6%, fixed $100 position, 15m. Testing must judge it; it is not claimed as the original author's exact strategy.
