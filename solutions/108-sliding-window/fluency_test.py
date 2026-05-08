"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.window_sums([1, 2, 3, 4, 5], 3) == [6, 9, 12]


def test_window_one():
    assert ex.window_sums([1, 2, 3], 1) == [1, 2, 3]


def test_window_eq_len():
    assert ex.window_sums([1, 2, 3], 3) == [6]


def test_window_too_big():
    assert ex.window_sums([1, 2, 3], 5) == []


def test_window_zero():
    assert ex.window_sums([1, 2, 3], 0) == []


def test_negatives():
    assert ex.window_sums([-1, -2, 3, -4, 5], 2) == [-3, 1, -1, 1]


def test_large_input_must_be_fast():
    """If still O(n*k), this would take forever. Slide makes it O(n)."""
    n = 50_000
    arr = [1] * n
    out = ex.window_sums(arr, 100)
    assert len(out) == n - 99
    assert all(s == 100 for s in out)
