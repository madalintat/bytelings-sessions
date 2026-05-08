"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_named_access():
    s = ex.stats([1, 2, 3, 4])
    assert s.count == 4
    assert s.total == 10
    assert s.mean == 2.5


def test_tuple_unpack_still_works():
    count, total, mean = ex.stats([1, 2, 3])
    assert (count, total, mean) == (3, 6, 2.0)


def test_empty():
    s = ex.stats([])
    assert s.count == 0
    assert s.total == 0
    assert s.mean == 0.0


def test_is_a_tuple():
    s = ex.stats([1])
    assert isinstance(s, tuple)


def test_class_name():
    s = ex.stats([1])
    assert type(s).__name__ == "Stats"
