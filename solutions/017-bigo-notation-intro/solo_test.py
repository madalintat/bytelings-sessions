"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import pytest
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.most_common([1, 2, 2, 3, 3, 3]) == 3


def test_tie_first_wins():
    assert ex.most_common(["a", "b", "a", "b"]) == "a"


def test_single():
    assert ex.most_common([42]) == 42


def test_all_same():
    assert ex.most_common([5, 5, 5]) == 5


def test_empty_raises():
    with pytest.raises(ValueError):
        ex.most_common([])


def test_strings():
    assert ex.most_common(["x", "y", "x", "z", "y", "y"]) == "y"


def test_large_input():
    items = [0] * 1000 + [1] * 999
    assert ex.most_common(items) == 0
