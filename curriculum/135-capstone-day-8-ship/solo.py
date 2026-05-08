"""Rung 4: Solo implement — graduation-log summary string.

Topic: P-07 accumulator-into-dict, sorted output

Implement `summary(findings: list[dict]) -> str` where `findings` is
the output of `parse_findings_log` from rung 3.

The returned string must have this exact shape:

    === Linter Findings Summary ===
    Total: <N> findings

    By rule (most frequent first):
      <rule>: <count>
      <rule>: <count>
      ...

    Top 3 affected files:
      <path>: <count> finding(s)
      <path>: <count> finding(s)
      <path>: <count> finding(s)

Rules sorted by count descending (ties: alphabetical).
Top-3 files sorted by count descending (ties: alphabetical).
Hidden tests check the structure and specific substrings.
"""
from __future__ import annotations


def summary(findings: list[dict]) -> str:
    """Return a multi-line graduation-log summary block."""
    raise NotImplementedError
