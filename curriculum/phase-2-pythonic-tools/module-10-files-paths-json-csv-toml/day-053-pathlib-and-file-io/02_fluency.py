"""Rung 2: Fluency drill — convert string-paths to pathlib.

Topic: pathlib.Path

`build_report_path(base, name)` should join `base` and a filename
`name + ".txt"` using `Path` and the / operator. It must return a
`Path` object, not a string.
"""
from pathlib import Path


def build_report_path(base: str, name: str) -> Path:
    """Return Path('<base>/<name>.txt')."""
    # TODO: stop building strings; use Path(base) / f"{name}.txt"
    return base + "/" + name + ".txt"
