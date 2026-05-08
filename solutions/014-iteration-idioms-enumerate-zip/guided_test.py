"""Tests for rung 3."""
import pytest
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_one_diff():
    assert ex.find_diffs([1, 2, 3], [1, 9, 3]) == [(1, 2, 9)]


def test_no_diffs():
    assert ex.find_diffs([1, 2, 3], [1, 2, 3]) == []


def test_all_diffs():
    assert ex.find_diffs([1, 2, 3], [9, 8, 7]) == [
        (0, 1, 9), (1, 2, 8), (2, 3, 7),
    ]


def test_empty():
    assert ex.find_diffs([], []) == []


def test_length_mismatch_raises():
    with pytest.raises(ValueError):
        ex.find_diffs([1, 2], [1, 2, 3])
    with pytest.raises(ValueError):
        ex.find_diffs([1], [])


def test_with_strings():
    assert ex.find_diffs(["a", "b"], ["a", "x"]) == [(1, "b", "x")]
