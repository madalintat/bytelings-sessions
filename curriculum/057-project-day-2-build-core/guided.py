"""Rung 3: Guided implement.

Topic: save_snapshots — atomic JSON output

Implement `save_snapshots(path, snapshots)`:
- Convert each Snapshot to a dict with dataclasses.asdict.
- json.dumps the list with indent=2, sort_keys=True.
- Write atomically to `path` using a `.tmp` sibling + os.replace.
- Use encoding="utf-8".

You can use any Snapshot-like dataclass — the test will pass its own.
"""
import dataclasses
import json
import os
from pathlib import Path


def save_snapshots(path: Path, snapshots: list) -> None:
    # TODO:
    #   1. Build payload = [dataclasses.asdict(s) for s in snapshots]
    #   2. text = json.dumps(payload, indent=2, sort_keys=True)
    #   3. Write text to a tmp path, then os.replace into place.
    raise NotImplementedError
