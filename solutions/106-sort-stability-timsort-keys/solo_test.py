"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_case_insensitive():
    assert ex.nice_sort(["banana", "apple", "Cherry"]) == ["apple", "banana", "Cherry"]


def test_preserves_tie_order():
    assert ex.nice_sort(["Banana", "apple", "banana", "Apple"]) == [
        "apple", "Apple", "Banana", "banana",
    ]


def test_all_same_word():
    out = ex.nice_sort(["abc", "ABC", "Abc", "aBc"])
    # All ties — output order should equal input order.
    assert out == ["abc", "ABC", "Abc", "aBc"]


def test_empty():
    assert ex.nice_sort([]) == []


def test_one():
    assert ex.nice_sort(["hi"]) == ["hi"]
