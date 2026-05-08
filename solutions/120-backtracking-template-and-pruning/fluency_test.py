"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _normalize(subsets_list):
    """Turn list of lists into a set of tuples for order-independent compare."""
    return {tuple(s) for s in subsets_list}


def test_basic():
    out = ex.subsets([1, 2, 3])
    expected = {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)}
    assert _normalize(out) == expected


def test_empty():
    assert ex.subsets([]) == [[]]


def test_one():
    out = ex.subsets([5])
    assert _normalize(out) == {(), (5,)}


def test_two():
    out = ex.subsets(["a", "b"])
    assert _normalize(out) == {(), ("a",), ("b",), ("a", "b")}


def test_count():
    """An n-element list has 2^n subsets."""
    assert len(ex.subsets([1, 2, 3, 4])) == 16
