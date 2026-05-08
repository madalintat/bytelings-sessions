"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_shift():
    assert ex.shift(ex.Coord(1, 2), 3, 4) == ex.Coord(4, 6)


def test_zero_shift_returns_equal():
    c = ex.Coord(5, 6)
    assert ex.shift(c, 0, 0) == c


def test_returns_a_coord():
    result = ex.shift(ex.Coord(0, 0), 1, 1)
    assert isinstance(result, ex.Coord)


def test_negative_shift():
    assert ex.shift(ex.Coord(0, 0), -3, -4) == ex.Coord(-3, -4)


def test_coord_is_hashable():
    """NamedTuple instances must be hashable — usable as dict keys."""
    d = {ex.Coord(1, 2): "first"}
    d[ex.Coord(3, 4)] = "second"
    assert d[ex.Coord(1, 2)] == "first"
