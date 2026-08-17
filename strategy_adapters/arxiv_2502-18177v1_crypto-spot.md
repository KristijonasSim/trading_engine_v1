# Strategy adapter: Recurrent Neural Networks for Dynamic VWAP Execution: Adaptive Trading Strategies with Temporal Kolmogorov-Arnold Networks

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: http://arxiv.org/abs/2502.18177v1
- Source market: `crypto`
- Author: Remi Genet
- Summary: The execution of Volume Weighted Average Price (VWAP) orders remains a critical challenge in modern financial markets, particularly as trading volumes and market complexity continue to increase. In my previous work arXiv:2502.13722, I introduced a novel deep learning approach that demonstrated significant improvements over traditional VWAP execution methods by directly optimizing the execution problem rather than relying on volume curve predictions. However, that model was static because it employed the fully linear approach described in arXiv:2410.21448, which is not designed for dynamic adjustment. This paper extends that foundation by developing a dynamic neural VWAP framework that adapts to evolving market conditions in real time. We introduce two key innovations: first, the integration of recurrent neural networks to capture complex temporal dependencies in market dynamics, and second, a sophisticated dynamic adjustment mechanism that continuously optimizes execution decisions based on market feedback. The empirical analysis, conducted across five major cryptocurrency markets, demonstrates that this dynamic approach achieves substantial improvements over both traditional methods and our previous static implementation, with execution performance gains of 10 to 15% in liquid markets and consistent outperformance across varying conditions. These results suggest that adaptive neural architectures can effectively address the challenges of modern VWAP execution while maintaining computational efficiency suitable for practical deployment.

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

- Result: Claude reviewed the public source; proposed volatility_regime rules: EMA 20/30, RSI entry > 58, exit < 48, stop-loss -8%, fixed $100 position, 5m. Testing must judge it; it is not claimed as the original author's exact strategy.
