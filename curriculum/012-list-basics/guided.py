"""Rung 3: Guided implement.

Topic: build a list with a loop and return its length

Implement `unique_in_order(items)`: return a new list of items with
consecutive duplicates removed, preserving order.
"""


def unique_in_order(items: list) -> list:
    """Drop consecutive duplicates; keep order.

    >>> unique_in_order([1, 1, 2, 2, 2, 3, 1])
    [1, 2, 3, 1]
    >>> unique_in_order([])
    []
    >>> unique_in_order(['a'])
    ['a']
    >>> unique_in_order(['a', 'a', 'a'])
    ['a']

    Note: this is NOT the same as set(items) — order matters and
    non-consecutive duplicates are kept.
    """
    # TODO: walk items, keep each one only if it differs from the last kept.
    raise NotImplementedError
