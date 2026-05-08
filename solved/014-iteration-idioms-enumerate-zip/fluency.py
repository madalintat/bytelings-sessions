"""Rung 2: Fluency — solved version.

Three iteration patterns that replace manual indexing:
  1. numbered_lines: `range(len(items))` + `items[i]` is the C-style loop.
     `enumerate(items, start=1)` yields (1, items[0]), (2, items[1]),
     etc. directly — more readable and idiomatic.
  2. pair_up: manual index access can be replaced by `zip(names, scores)`,
     which yields (name, score) pairs. No index needed.
  3. to_dict: `dict(zip(keys, values))` is the one-liner idiom.
     The test checks for "zip(" in the source.
"""


def numbered_lines(items: list[str]) -> list[str]:
    """Return ['1: alpha', '2: bravo', ...] (1-based)."""
    return [f"{i}: {item}" for i, item in enumerate(items, start=1)]


def pair_up(names: list[str], scores: list[int]) -> list[str]:
    """Return ['alice: 90', 'bob: 85', ...]."""
    return [f"{name}: {score}" for name, score in zip(names, scores)]


def to_dict(keys: list, values: list) -> dict:
    """Build a dict from parallel keys and values, in O(n)."""
    return dict(zip(keys, values))
