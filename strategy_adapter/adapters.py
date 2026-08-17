from __future__ import annotations

import re
from pathlib import Path
from typing import Any


def safe_filename(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:80] or "strategy"


def make_adapter(record: dict[str, Any], target: str) -> str:
    authors = ", ".join(record.get("authors", [])) or "Unknown"
    return f"""# Strategy adapter: {record.get('short_title') or record['title']}

## Status

- Status: `draft`
- Target: `{target}`
- Testing handoff: `blocked`

## Original source

- Link: {record['url']}
- Source market: `{record.get('market', 'other')}`
- Author: {authors}
- Summary: {record.get('summary') or 'Read source'}

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
"""


def write_adapter(record: dict[str, Any], target: str, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{safe_filename(record['source'])}_{safe_filename(record['id'])}_{target}.md"
    path.write_text(make_adapter(record, target), encoding="utf-8")
    return path
