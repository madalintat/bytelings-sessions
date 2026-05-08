"""Rung 3: Guided — solved version.

`argmax` tracks the index of the best element seen so far. Using a
`key` function lets callers compare by a derived value (e.g. len) without
modifying the input.

Design choices:
  - Raise ValueError on empty input (consistent with Python's max() behaviour).
  - Walk from left to right; use strict `>` (not `>=`) so that on a tie the
    FIRST (smallest-index) occurrence wins — it was set on the initial
    assignment and is never replaced by an equal value.
  - The `key` default of None is handled via a conditional in the comparison.

Alternative: `max(range(len(items)), key=lambda i: key(items[i]) if key else items[i])`
works in one line but is harder to read.
"""
from typing import Callable


def argmax(items: list, key: Callable | None = None) -> int:
    """Return the index of the max item. On ties, the smallest index wins.

    >>> argmax([3, 1, 4, 1, 5, 9, 2, 6])
    5
    >>> argmax([1, 1, 1])
    0
    >>> argmax(['bee', 'a', 'carrot'], key=len)
    2
    """
    if not items:
        raise ValueError("argmax of empty list")
    best_i = 0
    best_v = key(items[0]) if key else items[0]
    for i in range(1, len(items)):
        v = key(items[i]) if key else items[i]
        if v > best_v:
            best_i = i
            best_v = v
    return best_i
