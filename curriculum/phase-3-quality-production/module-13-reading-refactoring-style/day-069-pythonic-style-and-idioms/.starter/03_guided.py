"""Rung 3: Guided implement — use defaultdict and dict comprehensions.

Topic: more idioms. Same behavior, less ceremony.

Real-world framing: a tiny log analyzer that counts events per level
and computes the percentage of each.
"""
from collections import defaultdict


def count_levels(lines: list[str]) -> dict[str, int]:
    """Count occurrences of each level (first token of the line).

    Lines look like: "INFO request handled" / "ERROR db down".
    Lines with no whitespace are ignored.

    Hint: collections.defaultdict(int) lets you write
        counts[level] += 1
    without first checking whether the key exists.
    """
    # TODO: use defaultdict(int).
    raise NotImplementedError


def percentages(counts: dict[str, int]) -> dict[str, float]:
    """Convert {level: count} -> {level: pct} where pct is 0..100,
    rounded to one decimal. Empty input -> {}.

    Hint: a dict comprehension fits in one line.
    """
    # TODO: dict comprehension.
    raise NotImplementedError
