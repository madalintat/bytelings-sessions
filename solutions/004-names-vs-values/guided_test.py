"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_same_object():
    x = [1, 2, 3]
    assert ex.same_list(x, x) is True


def test_equal_but_different_object():
    assert ex.same_list([1, 2, 3], [1, 2, 3]) is False


def test_different_values():
    assert ex.same_list([1], [2]) is False


def test_works_with_dicts_too():
    d = {"a": 1}
    assert ex.same_list(d, d) is True
