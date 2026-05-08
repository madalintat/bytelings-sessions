"""Rung 2: Fluency — solved version.

`typing.NamedTuple` turns a class definition into a tuple subclass.
The fields (count, total, mean) become positional tuple slots but are
also accessible by name. The function returns `Stats(...)` instead of
a plain `(n, total, mean)` — tuple unpacking still works because
NamedTuple *is* a tuple.
"""
from typing import NamedTuple


class Stats(NamedTuple):
    count: int
    total: int
    mean: float


def stats(values: list[int]) -> Stats:
    """Return count, total, and mean for `values`.

    For an empty list, mean is 0.0.
    """
    n = len(values)
    total = sum(values)
    mean = total / n if n else 0.0
    return Stats(count=n, total=total, mean=mean)
