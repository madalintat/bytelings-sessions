"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_present():
    assert ex.has_pair_with_sum([1, 2, 3, 4], 5) is True


def test_absent():
    assert ex.has_pair_with_sum([1, 2, 3], 100) is False


def test_duplicate_ok():
    assert ex.has_pair_with_sum([3, 3], 6) is True


def test_single_not_paired_with_self():
    """We need TWO distinct indices, not one used twice."""
    assert ex.has_pair_with_sum([5], 10) is False


def test_empty():
    assert ex.has_pair_with_sum([], 0) is False


def test_negative_numbers():
    assert ex.has_pair_with_sum([-1, 2, 3], 1) is True


def test_runs_on_large_input():
    """If you wrote the O(n^2) loop, this would still finish but slow.
    The point is correctness; speed is the takeaway."""
    nums = list(range(10_000))
    assert ex.has_pair_with_sum(nums, 19_997) is True  # 9998 + 9999
