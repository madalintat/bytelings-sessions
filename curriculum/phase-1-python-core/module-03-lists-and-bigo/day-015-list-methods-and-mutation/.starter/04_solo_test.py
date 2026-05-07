"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.dedupe([1, 2, 1, 3, 2, 4]) == [1, 2, 3, 4]


def test_strings():
    assert ex.dedupe(["a", "b", "a", "c"]) == ["a", "b", "c"]


def test_empty():
    assert ex.dedupe([]) == []


def test_no_duplicates():
    assert ex.dedupe([1, 2, 3]) == [1, 2, 3]


def test_all_duplicates():
    assert ex.dedupe([1, 1, 1, 1]) == [1]


def test_mixed_types():
    assert ex.dedupe([1, "1", 1, "1"]) == [1, "1"]


def test_does_not_mutate():
    src = [1, 2, 1, 3]
    ex.dedupe(src)
    assert src == [1, 2, 1, 3]


def test_preserves_first_occurrence_order():
    assert ex.dedupe([3, 1, 2, 1, 3, 2]) == [3, 1, 2]
