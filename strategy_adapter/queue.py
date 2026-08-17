"""Local, paused queue for future automatic strategy adaptation."""
from __future__ import annotations
import json
from datetime import UTC, datetime
from pathlib import Path

def path(root: Path) -> Path: return root / "data" / "adapter" / "queue.json"
def load(root: Path) -> dict:
    try: return json.loads(path(root).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError): return {"paused": True, "items": [], "log": ["Adapter is paused. LLM is not configured."]}
def save(root: Path, state: dict) -> None:
    path(root).parent.mkdir(parents=True, exist_ok=True); path(root).write_text(json.dumps(state, indent=2)+"\n", encoding="utf-8")
def add(root: Path, source: str, record_id: str, title: str, target: str) -> dict:
    state=load(root)
    if not any(x["source"]==source and x["id"]==record_id for x in state["items"]):
        state["items"].append({"source":source,"id":record_id,"title":title,"target":target,"status":"waiting","added_at":datetime.now(UTC).isoformat()})
        state["log"].insert(0, f"Queued: {title}")
    save(root,state); return state
