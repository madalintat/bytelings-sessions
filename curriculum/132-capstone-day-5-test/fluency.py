"""Rung 2: Fluency drill — fix the finding formatter.

Topic: f-string formatting, de facto linter wire format

The real format used by ruff, flake8, mypy and friends is:
    path:line:col: rule-id: message

The current implementation produces the wrong shape. Fix it.
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
    """Return a single-line string for `f` in the standard linter format.

    Expected:  path:line:col: rule-id: message
    Current:   [path] line=N col=N rule: message   ← wrong shape
    """
    # TODO: fix this f-string to match `path:line:col: rule_id: message`
    return f"[{f.path}] line={f.line} col={f.col} rule: {f.message}"
