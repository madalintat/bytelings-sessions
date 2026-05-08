"""Rung 2: Fluency — solved version.

Two bugs fixed:
1. `load_config` used `eval()` — dangerous and wrong. `json.loads`
   parses JSON safely.
2. `save_config` called `json.dumps` without `indent`. Adding
   `indent=2` makes the output human-readable.
"""
import json
from pathlib import Path


def load_config(path: Path) -> dict:
    """Read JSON from `path` and return a dict."""
    return json.loads(path.read_text())


def save_config(path: Path, data: dict) -> None:
    """Write `data` as JSON, indented 2."""
    path.write_text(json.dumps(data, indent=2))
