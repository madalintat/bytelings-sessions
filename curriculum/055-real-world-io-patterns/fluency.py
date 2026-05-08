"""Rung 2: Fluency drill — make save_report safe.

Topic: atomic write + explicit encoding

`save_report(path, text)` should write `text` to `path`:
1. Atomically (write to a .tmp sibling, then os.replace).
2. With explicit utf-8 encoding (so Windows colleagues don't get garbled output).
"""
import os
from pathlib import Path


def save_report(path: Path, text: str) -> None:
    """Write `text` to `path` atomically with utf-8 encoding."""
    # TODO: 1) write to path.with_suffix(path.suffix + ".tmp")
    #       2) pass encoding="utf-8"
    #       3) os.replace(tmp, path) to make it atomic
    path.write_text(text)
