# Strategy adapter: Swing-Trading Risk Magnitude

## Status

- Status: `ai_hypothesis`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://doi.org/10.2139/ssrn.4574554
- Source market: `general`
- Author: Stoyan Angelov
- Summary: In this extended abstract, the Swing-Trading Risk Magnitude (STRM) is introduced as a novel method for quantifying risk. The STRM quantifies risk under the assumption that one is engaging in monthly swing-trading: a long position is opened during some upward momentum and not closed for at least several months. Because of this assumption, the STRM is tailored toward what is likely the average swing-trading retail investor. The STRM is calculated using the magnitude of a “volatility vector” and scaling it by an autocorrelation coefficient. As a result, the STRM is easy to interpret because of its linear properties.

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

- Result: Source page could not be read; proposed volatility_regime rules: EMA 20/49, RSI entry > 49, exit < 52, stop-loss -8%, fixed $100 position, 1h. Testing must judge it; it is not claimed as the original author's exact strategy.
