"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.reverse_in_place([1, 2, 3, 4]) == [4, 3, 2, 1]


def test_odd_length():
    assert ex.reverse_in_place([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


def test_empty():
    assert ex.reverse_in_place([]) == []


def test_one():
    assert ex.reverse_in_place([42]) == [42]


def test_two():
    assert ex.reverse_in_place(["a", "b"]) == ["b", "a"]


def test_in_place():
    arr = [1, 2, 3]
    ret = ex.reverse_in_place(arr)
    assert ret is arr
