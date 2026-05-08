"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    assert ex.find_pair_with_sum([1, 2, 3, 4], 5) == (0, 3)


def test_no_pair():
    assert ex.find_pair_with_sum([1, 2, 3, 4], 100) is None


def test_empty():
    assert ex.find_pair_with_sum([], 0) is None


def test_single():
    assert ex.find_pair_with_sum([5], 5) is None


def test_duplicate_values():
    assert ex.find_pair_with_sum([3, 3], 6) == (0, 1)


def test_picks_smallest_i_then_smallest_j():
    # Multiple pairs sum to 5: (0,3) via 1+4, (1,2) via 2+3
    # Smallest i is 0, so (0, 3) wins.
    assert ex.find_pair_with_sum([1, 2, 3, 4], 5) == (0, 3)


def test_negative_numbers():
    assert ex.find_pair_with_sum([-2, 1, 4, 3], 1) == (0, 2)


def test_zero_target():
    assert ex.find_pair_with_sum([0, 0, 1], 0) == (0, 1)
