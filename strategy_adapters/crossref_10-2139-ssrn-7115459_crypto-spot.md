# Strategy adapter: Risk-Managed Crypto Momentum

## Status

- Status: `adapted`
- Target: `crypto-spot`
- Testing handoff: `ready`

## Original source

- Link: https://doi.org/10.2139/ssrn.7115459
- Source market: `crypto`
- Author: Joseph Howden, Maksim Aleksandrovich Andreev
- Summary: We study a fixed-lookback (L = 30 day) long/cash time-series-momentum (TSMOM) sleeve on liquid crypto-majors (BTC, ETH, BNB, XRP, ADA, SOL, DOGE), overlaid with a market-drawdown-state de-risking rule. The construction follows Moskowitz, Ooi and Pedersen (2012): hold each asset only while its trailing 30-day cumulative log-return is positive, otherwise rotate that allocation to cash; then scale the whole book's gross exposure down (×0.5) when the aggregate crypto market is more than 15% off its trailing peak. The headline finding is a drawdown-control result, not an alpha result. Across an offline 96-configuration grid, 100% of configurations produced a smaller maximum drawdown than equal-weight buy-and-hold; in an out-of-sample (OOS) walk-forward test with the lookback fixed a priori at L = 30, the sleeve delivered net-of-25bps Sharpe 1.41 (Harvey-Liu-Zhu t = 3.21) versus buy-and-hold Sharpe 0.70 (t = 1.60), with maximum drawdown cut roughly in half (-44.6% vs-84.4%). Adding the drawdown-state de-risk overlay (×0.5 beyond 15% off-peak) further reduced maximum drawdown to about-28% and lifted Calmar from roughly 1.56 to 1.98 while holding Sharpe near 1.53 (t = 3.69). The effect survives a frozen long-history (survivorshiphardened) universe and a 50bps round-trip cost assumption. We are explicit that this is risk-managed β-a documented trend premium with crash protection-not market-neutral alpha; that vol-targeting / Kelly sizing on top of this sleeve was tested and SETTLED NULL (it de-levers the payoff engine); that the L = 30 optimum is a recorded, accepted sharp-parameter fragility; that absolute returns are survivorship-inflated; and that the forward Harvey t &gt; 3 promotion bar has NOT yet been cleared (the sleeve is paper-only and forward-accruing).

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

- Result: Created BtcThirtyDayMomentum: BTC/USDT 30-day long/cash momentum on 1d candles.
