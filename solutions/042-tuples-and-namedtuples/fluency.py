"""Rung 2: Fluency drill — replace a tuple-by-position with a NamedTuple.

Topic: typing.NamedTuple

`stats(values)` currently returns a 3-tuple. Define a NamedTuple
called `Stats` with fields `count`, `total`, `mean`, and have `stats`
return a `Stats` instance instead. The tests check both name access
and tuple-unpack still work.
"""
from typing import NamedTuple


# TODO: define a NamedTuple `Stats` with fields:
#       count: int, total: int, mean: float


def stats(values: list[int]):
    """Return count, total, and mean for `values`.

    For an empty list, mean is 0.0.
    """
    n = len(values)
    total = sum(values)
    mean = total / n if n else 0.0
    # TODO: return a Stats(...) instead of a plain 3-tuple.
    return (n, total, mean)
