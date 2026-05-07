"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.unique_in_order([1, 1, 2, 2, 2, 3, 1]) == [1, 2, 3, 1]


def test_empty():
    assert ex.unique_in_order([]) == []


def test_single():
    assert ex.unique_in_order(["a"]) == ["a"]


def test_all_same():
    assert ex.unique_in_order(["a", "a", "a"]) == ["a"]


def test_no_dups():
    assert ex.unique_in_order([1, 2, 3]) == [1, 2, 3]


def test_strings():
    assert ex.unique_in_order(["aa", "aa", "bb", "aa"]) == ["aa", "bb", "aa"]


def test_does_not_mutate_input():
    src = [1, 1, 2]
    ex.unique_in_order(src)
    assert src == [1, 1, 2]
