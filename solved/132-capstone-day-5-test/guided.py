"""Rung 3: Guided implement — solved version.

sorted() returns a new list; the input is left untouched.
str(f.path) coerces Path to string so cross-platform separators sort correctly.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Finding:
    path: Path
    line: int
    col: int
    rule_id: str
    message: str


def sort_findings(findings: list[Finding]) -> list[Finding]:
    """Return a new list sorted by (path, line, col)."""
    # str(path) ensures consistent lexicographic ordering across OS separators.
    return sorted(findings, key=lambda f: (str(f.path), f.line, f.col))
