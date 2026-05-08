"""Rung 4: Solo — solved version.

`MinMax` is a NamedTuple — two fields, both ints. `min_max` delegates
to Python's built-in `min` and `max`, which are O(n) single-pass.
The empty guard raises ValueError before either built-in is called.
"""
from typing import NamedTuple


class MinMax(NamedTuple):
    lo: int
    hi: int


def min_max(values: list[int]) -> MinMax:
    if not values:
        raise ValueError("min_max requires a non-empty list")
    return MinMax(lo=min(values), hi=max(values))
