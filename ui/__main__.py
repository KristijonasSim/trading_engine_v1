"""Run the local dashboard at http://127.0.0.1:8000."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import threading
from datetime import UTC, datetime
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from research_engine.collectors import COLLECTORS, classify_market, expand_query, is_strategy_source, new_result_file, search

from .dashboard import create_adapter, dashboard_data, delete_source
from testing_engine.__main__ import update_job, validate
from testing_engine.worker import run_ready
from strategy_adapter.queue import add as add_to_queue
from strategy_adapter.automatic import adapt_all, adapt_one, find_all_rules, find_rules

PROJECT_ROOT = Path(__file__).resolve().parent.parent
STATIC_DIR = Path(__file__).resolve().parent / "static"


def recover_and_test(filename: str) -> None:
    find_rules(PROJECT_ROOT, filename)
    run_ready(PROJECT_ROOT)


def recover_all_and_test() -> None:
    find_all_rules(PROJECT_ROOT)
    run_ready(PROJECT_ROOT)


class DashboardHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def send_json(self, payload: object, status: int = HTTPStatus.OK) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if urlparse(self.path).path == "/api/dashboard":
            self.send_json(dashboard_data(PROJECT_ROOT))
            return
        if self.path == "/":
            self.path = "/index.html"
        super().do_GET()

    def do_POST(self) -> None:
        if urlparse(self.path).path not in {"/api/search", "/api/delete-source", "/api/create-adapter", "/api/queue-adapter", "/api/start-test", "/api/adapt-all", "/api/adapt-one", "/api/find-rules", "/api/find-all-rules"}:
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        try:
            size = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(size))
        except (ValueError, json.JSONDecodeError):
            self.send_json({"error": "Invalid JSON."}, HTTPStatus.BAD_REQUEST)
            return
        if urlparse(self.path).path == "/api/search":
            self.handle_search(payload)
        elif urlparse(self.path).path == "/api/delete-source":
            self.handle_delete_source(payload)
        elif urlparse(self.path).path == "/api/create-adapter":
            self.handle_create_adapter(payload)
        elif urlparse(self.path).path == "/api/queue-adapter":
            self.handle_queue_adapter(payload)
        elif urlparse(self.path).path == "/api/adapt-all":
            self.handle_adapt_all()
        elif urlparse(self.path).path == "/api/adapt-one":
            self.handle_adapt_one(payload)
        elif urlparse(self.path).path == "/api/find-rules":
            self.handle_find_rules(payload)
        elif urlparse(self.path).path == "/api/find-all-rules":
            self.handle_find_all_rules()
        else:
            self.handle_start_test(payload)

    def handle_search(self, payload: dict) -> None:
        query = str(payload.get("query", "")).strip()
        search_query = expand_query(query)
        source = str(payload.get("source", "all"))
        market = str(payload.get("market", "all"))
        try:
            limit = int(payload.get("limit", 5))
        except (TypeError, ValueError):
            limit = 0
        if not query or source not in {*COLLECTORS, "all"} or market not in {"all", "crypto", "stocks", "futures", "forex"} or not 1 <= limit <= 20:
            self.send_json({"error": "Use a query, valid source and market, and limit from 1 to 20."}, HTTPStatus.BAD_REQUEST)
            return
        sources = list(COLLECTORS) if source == "all" else [source]
        records = []
        errors = []
        for source_name in sources:
            try:
                records.extend(
                    record
                    for record in search(source_name, search_query, limit)
                    if is_strategy_source(record, search_query)
                    and (market == "all" or classify_market(record) == market)
                )
            except Exception as error:
                errors.append(f"{source_name}: {error}")
        if not records:
            scope = "all markets" if market == "all" else market
            self.send_json(
                {
                    "error": f"No {scope} strategy sources found. Try Everything if you want ideas from every market.",
                    "details": errors,
                },
                HTTPStatus.BAD_GATEWAY,
            )
            return
        output_dir = PROJECT_ROOT / "data" / "research"
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / new_result_file(query, source)
        output_path.write_text(
            json.dumps({"query": query, "search_query": search_query, "market": market, "created_at": datetime.now(UTC).isoformat(), "records": records}, indent=2) + "\n",
            encoding="utf-8",
        )
        self.send_json({"saved": str(output_path.relative_to(PROJECT_ROOT)), "search_query": search_query, "errors": errors, "dashboard": dashboard_data(PROJECT_ROOT)})

    def handle_delete_source(self, payload: dict) -> None:
        source = str(payload.get("source", ""))
        record_id = str(payload.get("id", ""))
        if not source or not record_id:
            self.send_json({"error": "Source and ID are required."}, HTTPStatus.BAD_REQUEST)
            return
        delete_source(PROJECT_ROOT, source, record_id)
        self.send_json({"dashboard": dashboard_data(PROJECT_ROOT)})

    def handle_create_adapter(self, payload: dict) -> None:
        target = str(payload.get("target", ""))
        if target not in {"crypto-spot", "crypto-futures"}:
            self.send_json({"error": "Choose crypto spot or crypto futures."}, HTTPStatus.BAD_REQUEST)
            return
        path = create_adapter(PROJECT_ROOT, str(payload.get("source", "")), str(payload.get("id", "")), target)
        if path is None:
            self.send_json({"error": "Source not found."}, HTTPStatus.NOT_FOUND)
            return
        threading.Thread(target=recover_and_test, args=(path.name,), daemon=True).start()
        self.send_json({"created": str(path.relative_to(PROJECT_ROOT)), "dashboard": dashboard_data(PROJECT_ROOT)})

    def handle_queue_adapter(self, payload: dict) -> None:
        source, record_id, title, target = (str(payload.get(k, "")) for k in ("source", "id", "title", "target"))
        if target not in {"crypto-spot", "crypto-futures"}: self.send_json({"error":"Choose a target."}, HTTPStatus.BAD_REQUEST); return
        add_to_queue(PROJECT_ROOT, source, record_id, title, target)
        self.send_json({"dashboard": dashboard_data(PROJECT_ROOT)})

    def handle_start_test(self, payload: dict) -> None:
        name = str(payload.get("strategy", ""))
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{0,79}", name):
            self.send_json({"error": "Invalid strategy name."}, HTTPStatus.BAD_REQUEST)
            return
        update_job(name, "queued", "Waiting for the Freqtrade worker to start.")
        if validate(name) != 0:
            update_job(name, "blocked", "Strategy failed the local test contract.")
            self.send_json({"error": "This strategy is not ready for testing.", "dashboard": dashboard_data(PROJECT_ROOT)}, HTTPStatus.CONFLICT)
            return
        subprocess.Popen(
            [sys.executable, "-m", "testing_engine", "run-timeframe-comparison", name],
            cwd=PROJECT_ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
        self.send_json({"dashboard": dashboard_data(PROJECT_ROOT)})

    def handle_adapt_all(self) -> None:
        result = adapt_all(PROJECT_ROOT)
        self.send_json({"result": result, "dashboard": dashboard_data(PROJECT_ROOT)})

    def handle_adapt_one(self, payload: dict) -> None:
        try:
            result = adapt_one(PROJECT_ROOT, str(payload.get("file", "")))
        except ValueError as error:
            self.send_json({"error": str(error)}, HTTPStatus.NOT_FOUND)
            return
        self.send_json({"result": result, "dashboard": dashboard_data(PROJECT_ROOT)})

    def handle_find_rules(self, payload: dict) -> None:
        try:
            filename = str(payload.get("file", ""))
            result = find_rules(PROJECT_ROOT, filename)
        except ValueError as error:
            self.send_json({"error": str(error)}, HTTPStatus.NOT_FOUND)
            return
        if result == "ai_hypothesis":
            threading.Thread(target=run_ready, args=(PROJECT_ROOT,), daemon=True).start()
        self.send_json({"result": result, "dashboard": dashboard_data(PROJECT_ROOT)})

    def handle_find_all_rules(self) -> None:
        threading.Thread(target=recover_all_and_test, daemon=True).start()
        self.send_json({"message": "Autonomous rule-recovery and testing worker started.", "dashboard": dashboard_data(PROJECT_ROOT)})

    def log_message(self, format: str, *args) -> None:
        message = format % args
        if "/api/dashboard" not in message:
            print(f"Dashboard: {message}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the local trading-engine dashboard.")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), DashboardHandler)
    print(f"Dashboard running at http://127.0.0.1:{args.port}")
    print("Press Ctrl+C to stop it.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDashboard stopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
