"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    arr = [1, 1, 2, 3, 3, 3, 4]
    k = ex.remove_duplicates(arr)
    assert k == 4
    assert arr[:k] == [1, 2, 3, 4]


def test_no_dupes():
    arr = [1, 2, 3, 4]
    k = ex.remove_duplicates(arr)
    assert k == 4
    assert arr[:k] == [1, 2, 3, 4]


def test_all_same():
    arr = [7, 7, 7, 7]
    k = ex.remove_duplicates(arr)
    assert k == 1
    assert arr[:k] == [7]


def test_empty():
    arr = []
    k = ex.remove_duplicates(arr)
    assert k == 0


def test_one():
    arr = [42]
    k = ex.remove_duplicates(arr)
    assert k == 1
    assert arr[:k] == [42]


def test_two_same():
    arr = [9, 9]
    k = ex.remove_duplicates(arr)
    assert k == 1
    assert arr[:k] == [9]
