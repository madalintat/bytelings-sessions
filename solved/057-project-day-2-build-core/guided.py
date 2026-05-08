"""Rung 3: Guided — solved version.

`dataclasses.asdict` converts each `Snapshot` to a plain dict
recursively. We write to a `.tmp` sibling then use `os.replace` for an
atomic swap. `sort_keys=True` makes the JSON deterministic across
Python versions.
"""
import dataclasses
import json
import os
from pathlib import Path


def save_snapshots(path: Path, snapshots: list) -> None:
    payload = [dataclasses.asdict(s) for s in snapshots]
    text = json.dumps(payload, indent=2, sort_keys=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)
