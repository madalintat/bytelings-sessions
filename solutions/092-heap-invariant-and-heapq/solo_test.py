"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_no_streams():
    assert ex.merge_k_sorted([]) == []


def test_single_empty_stream():
    assert ex.merge_k_sorted([[]]) == []


def test_one_stream():
    assert ex.merge_k_sorted([[1, 2, 3]]) == [1, 2, 3]


def test_three_disjoint_streams():
    out = ex.merge_k_sorted([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
    assert out == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_overlapping_values():
    out = ex.merge_k_sorted([[1, 1, 2], [1, 3, 3]])
    assert out == [1, 1, 1, 2, 3, 3]


def test_some_empty_streams():
    out = ex.merge_k_sorted([[1, 2], [], [3, 4], []])
    assert out == [1, 2, 3, 4]


def test_iterators_not_lists():
    out = ex.merge_k_sorted([iter([1, 4]), iter([2, 5]), iter([3])])
    assert out == [1, 2, 3, 4, 5]


def test_negatives():
    out = ex.merge_k_sorted([[-3, -1, 0], [-5, -2]])
    assert out == [-5, -3, -2, -1, 0]
