"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.unique_preserving_order([]) == []


def test_no_duplicates():
    assert ex.unique_preserving_order([1, 2, 3]) == [1, 2, 3]


def test_with_duplicates():
    assert ex.unique_preserving_order([1, 2, 1, 3, 2]) == [1, 2, 3]


def test_preserves_first_position():
    assert ex.unique_preserving_order(["b", "a", "b", "a", "c"]) == ["b", "a", "c"]


def test_does_not_mutate_input():
    original = [1, 2, 1, 3]
    ex.unique_preserving_order(original)
    assert original == [1, 2, 1, 3]


def test_returns_new_list():
    original = [1, 2, 3]
    result = ex.unique_preserving_order(original)
    assert result is not original
