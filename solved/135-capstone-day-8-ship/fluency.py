"""Rung 2: Fluency drill — solved version.

Two fixes:
  1. Split on ':' not ',' — commas don't appear in finding lines.
  2. Guard len(parts) >= 4 before indexing, and strip the rule value.
     The format is path:line:col: rule: message, so after split(':'),
     index 3 is ' rule-id' (with a leading space) — strip it.
"""
from __future__ import annotations

SAMPLE_FINDINGS = """\
src/main.py:10:4: bare-except: bare `except:` catches everything
src/main.py:22:0: unused-import: `os` imported but never used
src/utils.py:5:8: bare-except: bare `except:` catches everything
src/utils.py:31:0: unused-import: `sys` imported but never used
src/cli.py:14:0: unused-import: `json` imported but never used
"""


def count_by_rule(text: str) -> dict[str, int]:
    """Return {rule_id: count} for all findings in text."""
    counts: dict[str, int] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(":")   # fix 1: was split(",")
        if len(parts) < 4:        # fix 2: guard + strip
            continue
        rule = parts[3].strip()
        counts[rule] = counts.get(rule, 0) + 1
    return counts
