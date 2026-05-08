"""Rung 3: Guided implement — sort findings by (path, line, col).

Topic: sorting dataclasses with a key function

Define a `Finding` dataclass with fields:
    path:     Path
    line:     int
    col:      int
    rule_id:  str
    message:  str

Implement `sort_findings(findings)` that returns a new list sorted
by (str(path), line, col). Do NOT sort in-place — return a new list.

Hint:
    return sorted(findings, key=lambda f: (str(f.path), f.line, f.col))
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
    """Return findings sorted by (path, line, col).

    >>> f1 = Finding(Path("b.py"), 1, 0, "r", "m")
    >>> f2 = Finding(Path("a.py"), 5, 0, "r", "m")
    >>> [f.path.name for f in sort_findings([f1, f2])]
    ['a.py', 'b.py']
    """
    # TODO: return sorted(findings, key=lambda f: (str(f.path), f.line, f.col))
    raise NotImplementedError
