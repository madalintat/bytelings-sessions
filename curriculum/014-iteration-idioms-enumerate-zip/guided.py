"""Rung 3: Guided implement.

Topic: enumerate + zip combined

Implement `find_diffs(a, b)`: return a list of (index, a_val, b_val)
tuples for every position where the two lists differ.
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

    Raise ValueError if the lengths differ (use zip with strict=True
    OR check len() up front).
    """
    # TODO: use enumerate + zip; raise ValueError on length mismatch.
    raise NotImplementedError
