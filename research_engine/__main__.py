"""Command line entry point for Research Engine v1."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path

from .cards import write_card
from .collectors import COLLECTORS, classify_market, expand_query, is_strategy_source, new_result_file, search


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Find public strategy sources. No paid API is used.")
    commands = parser.add_subparsers(dest="command", required=True)

    search_parser = commands.add_parser("search", help="Search public source metadata.")
    search_parser.add_argument("query", help="Example: crypto momentum strategy")
    search_parser.add_argument("--source", choices=[*COLLECTORS, "all"], default="all")
    search_parser.add_argument("--market", choices=["all", "crypto", "stocks", "futures", "forex"], default="all")
    search_parser.add_argument("--limit", type=int, default=5, choices=range(1, 21))
    search_parser.add_argument("--output", type=Path, default=Path("data/research"))

    card_parser = commands.add_parser("create-card", help="Create a strategy card from one search record.")
    card_parser.add_argument("record_file", type=Path)
    card_parser.add_argument("--id", required=True, help="Exact source ID from the search result.")
    card_parser.add_argument("--output", type=Path, default=Path("strategy_cards"))
    return parser


def run_search(args: argparse.Namespace) -> int:
    search_query = expand_query(args.query)
    sources = list(COLLECTORS) if args.source == "all" else [args.source]
    all_records = []
    failures = []
    for source in sources:
        try:
            records = [
                record
                for record in search(source, search_query, args.limit)
                if is_strategy_source(record, search_query)
                and (args.market == "all" or classify_market(record) == args.market)
            ]
        except Exception as error:  # Network services can fail; the other sources may still work.
            failures.append(f"{source}: {error}")
            continue
        all_records.extend(records)
        print(f"{source}: {len(records)} records")

    if not all_records:
        print("No records saved.", file=sys.stderr)
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1

    args.output.mkdir(parents=True, exist_ok=True)
    path = args.output / new_result_file(args.query, args.source)
    payload = {
        "query": args.query,
        "search_query": search_query,
        "market": args.market,
        "created_at": datetime.now(UTC).isoformat(),
        "records": all_records,
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Saved {len(all_records)} records to {path}")
    for failure in failures:
        print(f"Warning: {failure}", file=sys.stderr)
    return 0


def run_create_card(args: argparse.Namespace) -> int:
    try:
        payload = json.loads(args.record_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"Cannot read record file: {error}", file=sys.stderr)
        return 1
    record = next((item for item in payload.get("records", []) if item.get("id") == args.id), None)
    if record is None:
        print("Source ID was not found in the record file.", file=sys.stderr)
        return 1
    path = write_card(record, args.output)
    print(f"Created {path}")
    return 0


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "search":
        return run_search(args)
    return run_create_card(args)


if __name__ == "__main__":
    raise SystemExit(main())
