# Strategy adapter: VWAP Execution with Signature-Enhanced Transformers: A Multi-Asset Learning Approach

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/2503.02680v1
- Source market: `crypto`
- Author: Remi Genet
- Summary: In this paper I propose a novel approach to Volume Weighted Average Price (VWAP) execution that addresses two key practical challenges: the need for asset-specific model training and the capture of complex temporal dependencies. Building upon my recent work in dynamic VWAP execution arXiv:2502.18177, I demonstrate that a single neural network trained across multiple assets can achieve performance comparable to or better than traditional asset-specific models. The proposed architecture combines a transformer-based design inspired by arXiv:2406.02486 with path signatures for capturing geometric features of price-volume trajectories, as in arXiv:2406.17890. The empirical analysis, conducted on hourly cryptocurrency trading data from 80 trading pairs, shows that the globally-fitted model with signature features (GFT-Sig) achieves superior performance in both absolute and quadratic VWAP loss metrics compared to asset-specific approaches. Notably, these improvements persist for out-of-sample assets, demonstrating the model's ability to generalize across different market conditions. The results suggest that combining global parameter sharing with signature-based feature extraction provides a scalable and robust approach to VWAP execution, offering significant practical advantages over traditional asset-specific implementations.

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

- Result: Claude reviewed the public source; proposed mean_reversion rules: EMA 15/51, RSI entry > 34, exit < 60, stop-loss -2%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
