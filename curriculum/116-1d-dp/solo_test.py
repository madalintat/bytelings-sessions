"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic_yes():
    assert ex.subset_sum([3, 34, 4, 12, 5, 2], 9) is True


def test_basic_no():
    assert ex.subset_sum([1, 2, 3], 7) is False


def test_empty_zero_target():
    assert ex.subset_sum([], 0) is True


def test_empty_nonzero_target():
    assert ex.subset_sum([], 5) is False


def test_zero_target_always_true():
    assert ex.subset_sum([1, 2, 3], 0) is True


def test_single_match():
    assert ex.subset_sum([7], 7) is True


def test_each_weight_used_once_only():
    """Can't reuse the 5 to make 10."""
    assert ex.subset_sum([5], 10) is False


def test_exact_total():
    assert ex.subset_sum([1, 2, 3, 4], 10) is True


def test_just_short():
    assert ex.subset_sum([1, 2, 3, 4], 11) is False
