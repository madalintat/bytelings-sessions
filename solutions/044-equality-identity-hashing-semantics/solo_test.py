"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.dedupe([1, 2, 1, 3, 2]) == [1, 2, 3]


def test_empty():
    assert ex.dedupe([]) == []


def test_preserves_first_occurrence_order():
    assert ex.dedupe(["b", "a", "b", "c", "a"]) == ["b", "a", "c"]


def test_no_dupes_unchanged():
    assert ex.dedupe([1, 2, 3]) == [1, 2, 3]


def test_unhashable_items_fallback():
    assert ex.dedupe([[1], [2], [1]]) == [[1], [2]]


def test_does_not_mutate_input():
    src = [1, 2, 1]
    ex.dedupe(src)
    assert src == [1, 2, 1]


def test_mixed_types():
    assert ex.dedupe([1, "1", 1, "1"]) == [1, "1"]
