"""Rung 3: Guided implement.

Topic: find the maximum yourself, with a tiebreaker

Implement `argmax(items, key=None)`: return the INDEX of the
maximum element. On ties, return the smallest index.
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
    >>> argmax([])
    Traceback (most recent call last):
        ...
    ValueError: argmax of empty list

    If `key` is None, compare items directly. Otherwise compare key(item).

    Raise ValueError on empty input.
    """
    # TODO: linear scan; track best_index and best_value.
    raise NotImplementedError
