"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert list(ex.Repeat([1, 2], 3)) == [1, 2, 1, 2, 1, 2]


def test_zero_times():
    assert list(ex.Repeat([1, 2], 0)) == []


def test_empty_values():
    assert list(ex.Repeat([], 5)) == []


def test_can_iterate_twice():
    r = ex.Repeat([7, 8], 2)
    assert list(r) == [7, 8, 7, 8]
    assert list(r) == [7, 8, 7, 8]


def test_iter_returns_fresh_iterator():
    r = ex.Repeat([1], 2)
    a = iter(r)
    b = iter(r)
    assert a is not b


def test_repeat_is_not_its_own_iterator():
    r = ex.Repeat([1], 1)
    assert not hasattr(r, "__next__")


def test_works_with_tuple_values():
    assert list(ex.Repeat((1, 2, 3), 2)) == [1, 2, 3, 1, 2, 3]
