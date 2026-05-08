"""Rung 3: Guided implement — parse findings log into structured dicts.

Topic: re.match per line, skip malformed

Each findings line has the format:
    path:line:col: rule-id: message

`parse_findings_log(text)` returns a list of dicts with keys:
    path, line, col, rule, message

Use `re.match` on each non-empty line. Silently skip lines that don't
match the pattern. `line` and `col` should be ints.

Fill in the function body. Use only stdlib (re).
"""
from __future__ import annotations
import re

# Matches: path : line : col : [space] rule-id : [space] message
_PATTERN = re.compile(
    r"^(?P<path>[^:]+)"
    r":(?P<line>\d+)"
    r":(?P<col>\d+)"
    r":\s*(?P<rule>[^:]+?)"
    r":\s*(?P<message>.+)$"
)


def parse_findings_log(text: str) -> list[dict]:
    """Return list of finding dicts; skip blank or malformed lines.

    Each dict has keys: path (str), line (int), col (int),
    rule (str), message (str).
    """
    # TODO: iterate text.splitlines(), call re.match(_PATTERN, line) on
    # each non-empty stripped line. If it matches, build a dict from the
    # named groups (convert line/col to int). Skip non-matching lines.
    raise NotImplementedError
