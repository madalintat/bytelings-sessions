"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: NamedTuple as a clear return type

Define a NamedTuple `MinMax` with fields `lo: int` and `hi: int`.

Then implement `min_max(values)`:
- For a non-empty list, return MinMax(lo=min(values), hi=max(values)).
- For an empty list, raise ValueError.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
from typing import NamedTuple


class MinMax(NamedTuple):
    pass  # TODO: replace with the actual fields


def min_max(values: list[int]) -> MinMax:
    raise NotImplementedError
