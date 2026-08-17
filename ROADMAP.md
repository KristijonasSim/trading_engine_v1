# Automatic Trading Plan

## Main decision

- Start with **one market only**: liquid crypto spot on one exchange.
- Start with **one bot stack**: [Freqtrade](https://github.com/freqtrade/freqtrade).
- Use [VectorBT](https://github.com/polakowo/vectorbt) only to quickly test many simple ideas.
- Keep real money off until the paper-trading gate passes.
- An LLM can find, explain, and code ideas. It must not approve a strategy by itself.

Why this start:

- Freqtrade has backtest, parameter search, dry-run, and live modes in one project.
- It also has a look-ahead test. This catches a common bug: using future price data by mistake. [Docs](https://docs.freqtrade.io/en/stable/lookahead-analysis/)
- VectorBT is fast for testing many inputs and settings. [Docs](https://vectorbt.dev/)

## The full flow

```text
Sources -> strategy cards -> quick tests -> hard tests -> paper bot -> small live bot
                 ^                                  |
                 +-------- results and notes -------+
```

### 1. Research engine

Goal: find ideas and turn them into clear strategy cards.

- Collect papers from [arXiv](https://info.arxiv.org/help/api/user-manual.html) and [Crossref](https://www.crossref.org/documentation/retrieve-metadata/rest-api/).
- Search open GitHub projects through the [GitHub API](https://docs.github.com/en/rest/search/search). Respect rate limits and every source license.
- Also collect exchange and data-provider documentation.
- Save the URL, author, date, license, market, and exact claim for every source.
- Do not copy private, paid, or unclear-license code into this project.
- Do not use web scraping when a site offers an API or says scraping is not allowed.

For each idea, create one short **strategy card**:

- Name and source URL.
- Market and timeframe.
- Entry rule, exit rule, stop rule, and position size rule.
- Data needed.
- Fees and delay assumptions.
- Why it could work.
- What would prove it wrong.

LLM job:

- Read source text and create the card.
- Turn a complete card into code in a locked test folder.
- Never invent missing rules. Mark them as `unknown` instead.
- Every LLM result needs a source link and a human review before tests run.

## 2. Testing engine

Goal: reject weak ideas before they can trade.

### Test order

1. **Quick screen** — VectorBT. Test simple rules across many coins and settings.
2. **Realistic test** — Freqtrade. Include exchange fees, spread, delay, and position limits.
3. **Bias checks** — run Freqtrade look-ahead analysis; check that data and indicators only use past values.
4. **Time split** — choose the rules on old data, then test once on newer hidden data.
5. **Walk-forward test** — repeat the old/new split through time.
6. **Stress test** — worse fees, worse fills, missing candles, and slow orders.
7. **Paper trading** — Freqtrade dry-run with live market data.

### Required pass rules

- Test at least several market periods: up, down, and flat.
- Include real fees and a worse-than-normal slippage estimate.
- Record every tested setting. Do not keep only the best one.
- Keep a final data period hidden until the strategy is frozen.
- Reject a strategy if small setting changes break it.
- Compare with buy-and-hold and a simple moving-average rule.
- Set a maximum loss, maximum daily loss, and maximum position size before paper trading.

Why this matters:

- Trying many ideas can make random luck look good. The paper *The Probability of Backtest Overfitting* explains this risk and proposes a test for it. [Paper](https://papers.ssrn.com/sol3/Papers.cfm?abstract_id=2326253)
- Historical profit is not proof of future profit.

### What to measure

- Return after fees.
- Largest loss from a peak (max drawdown).
- Number of trades and win/loss size.
- Results in each market period, not only the total.
- Return after worse fill assumptions.
- Paper-trading result versus backtest result.

## 3. Bot and improvement engine

Goal: run only approved strategies and make changes safely.

- One strategy version can be: `research`, `rejected`, `paper`, `live-small`, or `stopped`.
- The bot may run only a version marked `paper` or `live-small`.
- Freeze code, settings, data version, and test report for every approved version.
- Use a separate API key for the bot. Disable withdrawals on that key.
- Store keys outside Git. Add `.env` and data folders to `.gitignore` before any keys or data exist.
- Start live at the smallest allowed size. Raise size slowly only after a written review.
- Stop trading automatically on daily-loss, drawdown, data-feed, order, or balance-check failures.
- Log every signal, order, fill, error, and stop event.
- Re-run tests after any code, data, exchange, or rule change.

## Recommended tools

| Tool | Use now | Reason |
| --- | --- | --- |
| [Freqtrade](https://github.com/freqtrade/freqtrade) | Yes | Best first choice for a crypto strategy bot. Backtest, dry-run, parameter search, and live trading are together. |
| [VectorBT](https://github.com/polakowo/vectorbt) | Yes | Very fast first screen for many simple strategy settings. |
| [NautilusTrader](https://github.com/nautechsystems/nautilus_trader) | Later | Strong event-based testing and live trading, but more setup and learning. |
| [LEAN](https://github.com/QuantConnect/Lean) | Later / stocks | Good choice if the project moves to stocks, futures, or many asset types. It supports local research, backtests, optimization, and live runs. |

Do not use the same test engine as the only proof. Before real money, repeat the final test in a second engine or paper trade it long enough to compare results. Backtest engines can differ, especially around costs and fills.

## Build order

1. Pick one exchange, one spot market group, and one timeframe.
2. Add a `.gitignore` for secrets and downloaded market data.
3. Install Freqtrade in a separate environment and run its example strategy in backtest mode.
4. Create the strategy-card format and a source list.
5. Build a small source collector for arXiv, Crossref, and GitHub metadata.
6. Add a VectorBT quick-screen notebook or script.
7. Add a Freqtrade test command that saves each report.
8. Add pass/fail rules and a paper-trading checklist.
9. Run one strategy through the full path before adding more.

## Later decisions

- If you want stocks or futures, use LEAN instead of Freqtrade as the main bot engine.
- If you need high-detail order-book or multi-venue work, test NautilusTrader after the first workflow works.
- Do not build custom order execution until an existing bot tool blocks a real need.

## Sources checked

- [Freqtrade look-ahead analysis](https://docs.freqtrade.io/en/stable/lookahead-analysis/)
- [Freqtrade parameter search](https://www.freqtrade.io/en/stable/hyperopt/)
- [VectorBT documentation](https://vectorbt.dev/)
- [NautilusTrader documentation](https://nautilustrader.io/docs/)
- [LEAN repository](https://github.com/QuantConnect/Lean)
- [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/)
- [GitHub search API](https://docs.github.com/en/rest/search/search)
- [Backtest-overfitting paper](https://papers.ssrn.com/sol3/Papers.cfm?abstract_id=2326253)
