"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_returns_new_list_with_item():
    original = [1, 2]
    result = ex.append_safely(original, 3)
    assert result == [1, 2, 3]


def test_does_not_mutate_input():
    original = [1, 2]
    ex.append_safely(original, 3)
    assert original == [1, 2]   # input untouched


def test_result_is_different_object():
    original = [1, 2]
    result = ex.append_safely(original, 3)
    assert result is not original
