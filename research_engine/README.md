# Research Engine v1

This tool finds public source metadata and creates strategy cards.

- It searches arXiv, Crossref, and public GitHub repositories.
- It uses Python only. No paid LLM API is used.
- It does not trade, connect to an exchange, or handle keys.
- Search files are saved under `data/research/`. That folder is not committed to Git.

## Search

Run from the project root:

```bash
python3 -m research_engine search "crypto momentum strategy"
```

Search one source only:

```bash
python3 -m research_engine search "crypto mean reversion" --source arxiv --limit 10
```

## Create a strategy card

First open the saved JSON file. Copy a source `id`. Then run:

```bash
python3 -m research_engine create-card data/research/FILE.json --id SOURCE_ID
```

The card is saved in `strategy_cards/` and starts as `needs review`.

## Rules

- A source is not a profitable strategy.
- Read the source and check its license before reusing any code.
- Fill every `unknown` rule before sending a card to the testing engine.
- Never put exchange keys in this project.

## Test

```bash
python3 -m unittest discover -s tests -v
```
