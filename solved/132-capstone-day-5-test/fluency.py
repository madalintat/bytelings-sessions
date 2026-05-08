"""Rung 2: Fluency drill — solved version.

The standard linter wire format is path:line:col: rule-id: message.
Every field is separated by a colon. No brackets, no label= prefixes.
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


def format_finding(f: Finding) -> str:
    """Return `path:line:col: rule-id: message`."""
    return f"{f.path}:{f.line}:{f.col}: {f.rule_id}: {f.message}"
