"""Rung 4: Solo — solved version.

`folder.rglob("*")` yields every path under `folder` recursively.
We filter to regular files with `.is_file()` and find the maximum by
`stat().st_size`. Using `max()` with a key avoids building a
full sorted list.
"""
from pathlib import Path


def largest_file(folder: Path) -> Path | None:
    files = (p for p in folder.rglob("*") if p.is_file())
    try:
        return max(files, key=lambda p: p.stat().st_size)
    except ValueError:
        return None
