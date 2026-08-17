# Strategy adapter: yeshunyi Momentum

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://github.com/yeshunyi/crypto-momentum-strategy
- Source market: `crypto`
- Author: yeshunyi
- Summary: 基于价格涨速和成交量变化识别短期强势币种，结合市场波动率动态调整参数的自动化量化交易策略。

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

- Result: AI proposed slow_momentum rules: EMA 20/60, RSI entry > 56, exit < 44, stop-loss -10%, fixed $100 position, 1h. This is an independent test hypothesis, not a claim about the original author's exact rules.
