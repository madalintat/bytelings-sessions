"""Rung 3: Guided implement — solved version.

count_levels uses defaultdict(int) to avoid the "if key not in" check.
percentages is a one-line dict comprehension; empty input returns {}.
"""
from collections import defaultdict


def count_levels(lines: list[str]) -> dict[str, int]:
    """Count occurrences of each level (first token of the line)."""
    counts: dict[str, int] = defaultdict(int)
    for line in lines:
        parts = line.split(None, 1)
        if parts:
            counts[parts[0]] += 1
    return dict(counts)


def percentages(counts: dict[str, int]) -> dict[str, float]:
    """Convert {level: count} -> {level: pct} where pct is 0..100."""
    if not counts:
        return {}
    total = sum(counts.values())
    return {level: round(count / total * 100, 1) for level, count in counts.items()}
