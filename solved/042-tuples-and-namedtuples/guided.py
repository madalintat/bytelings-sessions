"""Rung 3: Guided — solved version.

`Coord._replace(x=..., y=...)` returns a new NamedTuple with the
changed fields — the cleanest idiom when you have many fields and only
change a subset. A plain `Coord(coord.x + dx, coord.y + dy)` also
works and is equally idiomatic for small structs.
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
    return coord._replace(x=coord.x + dx, y=coord.y + dy)
