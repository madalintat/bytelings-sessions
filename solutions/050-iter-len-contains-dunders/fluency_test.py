"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_len():
    b = ex.Bag(["a", "b", "c"])
    assert len(b) == 3


def test_len_empty():
    assert len(ex.Bag()) == 0


def test_contains():
    b = ex.Bag(["x", "y"])
    assert "x" in b
    assert "z" not in b


def test_iteration():
    b = ex.Bag([1, 2, 3])
    assert list(b) == [1, 2, 3]


def test_can_iterate_twice():
    b = ex.Bag([1, 2])
    assert list(b) == [1, 2]
    assert list(b) == [1, 2]


def test_truthiness():
    """A Bag with __len__ should be falsy when empty, truthy otherwise."""
    assert not ex.Bag()
    assert ex.Bag([1])
