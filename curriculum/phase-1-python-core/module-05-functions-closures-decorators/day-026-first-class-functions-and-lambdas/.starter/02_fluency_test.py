"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_apply_basic():
    assert ex.apply(lambda x: x + 1, 5) == 6
    assert ex.apply(str.upper, "hello") == "HELLO"


def test_sort_by_length():
    assert ex.sort_by_length(["bee", "a", "carrot"]) == ["a", "bee", "carrot"]


def test_sort_by_length_ties_stable():
    assert ex.sort_by_length(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]


def test_keep_truthy_basic():
    assert ex.keep_truthy([1, 2, 3, 4, 5], lambda x: x % 2 == 0) == [2, 4]


def test_keep_truthy_returns_list():
    assert isinstance(ex.keep_truthy([1, 2], lambda x: True), list)


def test_keep_truthy_empty():
    assert ex.keep_truthy([], lambda x: True) == []


def test_double_each():
    assert ex.double_each([1, 2, 3]) == [2, 4, 6]


def test_double_each_empty():
    assert ex.double_each([]) == []
