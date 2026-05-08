"""Rung 2: Fluency — solved version.

Three steps for an atomic write:
1. Write to a `.tmp` sibling so a crash mid-write leaves the original
   intact.
2. Pass `encoding="utf-8"` explicitly — platform-default encoding can
   differ on Windows.
3. `os.replace(tmp, path)` is an atomic rename on POSIX and
   effectively atomic on Windows (replaces the destination in one
   syscall).
"""
import os
from pathlib import Path


def save_report(path: Path, text: str) -> None:
    """Write `text` to `path` atomically with utf-8 encoding."""
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)
