"""Create human-reviewable strategy cards from source records."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


def safe_filename(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:70] or "strategy"


def make_card(record: dict[str, Any]) -> str:
    authors = ", ".join(filter(None, record.get("authors", []))) or "Unknown"
    return f"""# Strategy card: {record['title']}

## Basic facts

- Status: `research`
- Source: [{record['source']}]({record['url']})
- Source ID: `{record['id']}`
- Author: {authors}
- Source date: {record.get('published') or 'Unknown'}
- Source license: {record.get('license') or 'Unknown — check before reuse'}
- Strategy version: `not coded`

## Source summary

{record.get('summary') or 'No summary was returned. Read the source before testing.'}

## Rules to confirm

- Market and pairs: `unknown`
- Timeframe: `unknown`
- Entry: `unknown`
- Exit: `unknown`
- Stop loss: `unknown`
- Position size: `unknown`
- Data and indicators needed: `unknown`

## Assumptions to set before testing

- Fee: `unknown`
- Slippage: `unknown`
- Order delay: `unknown`

## Human review

- Why this may work: `unknown`
- What would prove it wrong: `unknown`
- Decision: `needs review`
- Reviewer:
- Date:
"""


def write_card(record: dict[str, Any], output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{safe_filename(record['source'])}_{safe_filename(record['id'])}.md"
    path = output_dir / filename
    path.write_text(make_card(record), encoding="utf-8")
    return path
