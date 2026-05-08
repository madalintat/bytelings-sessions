"""Rung 3: Guided — solved version.

Use re.match with named groups for clean field extraction.
Convert line and col to int. Skip lines that don't match.
"""
from __future__ import annotations
import re

_PATTERN = re.compile(
    r"^(?P<path>[^:]+)"
    r":(?P<line>\d+)"
    r":(?P<col>\d+)"
    r":\s*(?P<rule>[^:]+?)"
    r":\s*(?P<message>.+)$"
)


def parse_findings_log(text: str) -> list[dict]:
    """Return list of finding dicts; skip blank or malformed lines."""
    results = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        m = re.match(_PATTERN, line)
        if not m:
            continue
        results.append({
            "path":    m.group("path"),
            "line":    int(m.group("line")),
            "col":     int(m.group("col")),
            "rule":    m.group("rule").strip(),
            "message": m.group("message").strip(),
        })
    return results
