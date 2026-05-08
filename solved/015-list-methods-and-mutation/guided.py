"""Rung 3: Guided — solved version.

`sort_by_length` delegates to `sorted()` with `key=len`. The `reverse`
parameter maps directly to `descending`. Since `sorted()` is stable,
equal-length strings maintain their original relative order.

The key insight: Python's sort is stable, meaning that equal elements
keep their original position. This is why `sort_by_length(["aa", "bb"])`
always returns `["aa", "bb"]` regardless of their relative order in the
input — all have the same key value, so stability preserves input order.
"""


def sort_by_length(strings: list[str], descending: bool = False) -> list[str]:
    """Return a new list sorted by string length.

    >>> sort_by_length(["bee", "a", "carrot"])
    ['a', 'bee', 'carrot']
    >>> sort_by_length(["bee", "a", "carrot"], descending=True)
    ['carrot', 'bee', 'a']
    >>> sort_by_length(["aa", "bb", "cc"])
    ['aa', 'bb', 'cc']
    """
    return sorted(strings, key=len, reverse=descending)
