"""Rung 2: Fluency — solved version.

`Path(base) / f"{name}.txt"` uses the `/` operator overloaded by
`pathlib.Path` to join path segments. The result is a `Path` object,
not a string — it knows about suffixes, parents, stems, etc.
"""
from pathlib import Path


def build_report_path(base: str, name: str) -> Path:
    """Return Path('<base>/<name>.txt')."""
    return Path(base) / f"{name}.txt"
