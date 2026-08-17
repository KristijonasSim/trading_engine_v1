# Strategy adapter: Momentum - Reversal Strategy

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://doi.org/10.2139/ssrn.1852585
- Source market: `stocks`
- Author: Hsin-Yi Yu, Li-Wen Chen
- Summary: Various theories have been presented to explain momentum and reversals in stock returns. Based on the model of Hong and Stein (1999), this paper creates a hybrid strategy to avoid the losses from the reversal phase. The risk-adjusted returns of the new strategy are significantly higher than those of the traditional momentum strategy. Moreover, the risk-adjusted returns of the new strategy cannot be fully explained by Carhart’s four-factor model. Such a finding is robust in different time periods and size quintiles. Overall, this paper exploits the interaction between heterogeneous investors and generates distinctive applications.

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

- Result: Source page could not be read; proposed factor_momentum rules: EMA 14/44, RSI entry > 46, exit < 42, stop-loss -9%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
