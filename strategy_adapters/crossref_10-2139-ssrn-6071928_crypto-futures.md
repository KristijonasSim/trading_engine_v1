# Strategy adapter: Automated Strategy Discovery in Crypto Perpetuals via Dynamic Factor Ensembles and Auditable Evaluation

## Status

- Status: `draft`
- Target: `crypto-futures`
- Testing handoff: `blocked`

## Original source

- Link: https://doi.org/10.2139/ssrn.6071928
- Source market: `futures`
- Author: Kaihong Deng
- Summary: Offline backtests are a central evaluation tool for data-driven decision policies, yet their apparent performance can collapse when evaluation mismatches deployment semantics (delays, costs, cash-flow accounting) or when repeated search reuses the same windows. We study automated strategy discovery in cryptocurrency perpetual futures, where fees, slippage, and funding cash flows can dominate profit and loss (PnL) for high-turnover policies. We present an end-to-end protocol that (i) maintains a dynamic, compact factor pool to control feature combinatorics, (ii) searches a modular policy family under STRICT T+1 execution with explicit cost and funding accounting, and (iii) selects configurations via robustness screening (cost stress) and walk-forward evaluation while exporting deterministic, machine-readable artifacts and invariant checks for auditability. From a knowledge-based systems perspective, the protocol represents evaluation semantics and selection rules as explicit knowledge objects, enabling traceable decision support and review. Across four liquid perpetual contracts (BTC/USDT, ETH/USDT, SOL/USDT, AVAX/USDT), we show that fee-only or zero-cost assumptions materially inflate apparent performance relative to a fully costed configuration. Under identical STRICT semantics, two-stage robustness screening tends to reduce drawdowns. Our contribution is validation infrastructure rather than a claim of persistent alpha: the protocol makes offline-to-deployment gaps and selection bias easier to detect, reproduce, and review.

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
