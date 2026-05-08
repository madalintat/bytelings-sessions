"""Rung 3: Guided implement.

Topic: NamedTuple as dict key + ._replace

Define a NamedTuple `Coord` with fields `x: int` and `y: int`.

Then implement `shift(coord, dx, dy)` that returns a new `Coord` whose
x is `coord.x + dx` and y is `coord.y + dy`. Use `Coord._replace(...)`
or simply construct a fresh `Coord(...)`. Don't mutate (you can't —
NamedTuples are immutable).
"""
from typing import NamedTuple


class Coord(NamedTuple):
    x: int
    y: int


def shift(coord: Coord, dx: int, dy: int) -> Coord:
    """Return a new Coord shifted by (dx, dy).

    >>> shift(Coord(1, 2), 3, 4)
    Coord(x=4, y=6)
    """
    # TODO: return a Coord with the shifted values.
    raise NotImplementedError
