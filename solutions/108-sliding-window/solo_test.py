"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.min_subarray_len([2, 3, 1, 2, 4, 3], 7) == 2


def test_impossible():
    assert ex.min_subarray_len([1, 1, 1, 1], 100) == 0


def test_single_element_works():
    assert ex.min_subarray_len([1, 4, 4], 4) == 1


def test_whole_array():
    assert ex.min_subarray_len([1, 2, 3], 6) == 3


def test_just_one_too_high():
    assert ex.min_subarray_len([1, 2, 3], 7) == 0


def test_empty():
    assert ex.min_subarray_len([], 5) == 0


def test_zero_target():
    """Any non-empty array satisfies target=0 with length 1."""
    assert ex.min_subarray_len([5, 1, 1], 0) == 1
