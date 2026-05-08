"""Rung 3: Guided — solved version.

`find_diffs` uses `enumerate(zip(a, b))` to walk both lists at once
with the index available:
  - `zip(a, b, strict=True)` raises ValueError if lengths differ.
    This is cleaner than a manual len() check.
  - `enumerate(...)` wraps the zip to get the index.

The result is a list of (i, a_val, b_val) tuples only for positions
that differ.
"""


def find_diffs(a: list, b: list) -> list[tuple[int, object, object]]:
    """Compare `a` and `b` element-wise; report positions that differ.

    >>> find_diffs([1, 2, 3], [1, 9, 3])
    [(1, 2, 9)]
    >>> find_diffs([1, 2, 3], [1, 2, 3])
    []
    >>> find_diffs([1, 2], [1, 2, 3])
    Traceback (most recent call last):
        ...
    ValueError: lists must be the same length
    """
    if len(a) != len(b):
        raise ValueError("lists must be the same length")
    return [
        (i, av, bv)
        for i, (av, bv) in enumerate(zip(a, b))
        if av != bv
    ]
