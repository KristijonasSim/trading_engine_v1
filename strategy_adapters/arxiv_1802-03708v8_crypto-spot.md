# Strategy adapter: Crypto Momentum Strategy

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/1802.03708v8
- Source market: `crypto`
- Author: Li Guo, Wolfgang Karl Härdle, Yubo Tao
- Summary: Cryptocurrencies return cross-predictability and technological similarity yield information on risk propagation and market segmentation. To investigate these effects, we build a time-varying network for cryptocurrencies, based on the evolution of return cross-predictability and technological similarities. We develop a dynamic covariate-assisted spectral clustering method to consistently estimate the latent community structure of cryptocurrencies network that accounts for both sets of information. We demonstrate that investors can achieve better risk diversification by investing in cryptocurrencies from different communities. A cross-sectional portfolio that implements an inter-crypto momentum trading strategy earns a 1.08% daily return. By dissecting the portfolio returns on behavioral factors, we confirm that our results are not driven by behavioral mechanisms.

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

- Result: Claude reviewed the public source; proposed trend_strength rules: EMA 8/42, RSI entry > 56, exit < 48, stop-loss -9%, fixed $100 position, 1d. Testing must judge it; it is not claimed as the original author's exact strategy.
