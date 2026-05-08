"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    result = ex.min_max([3, 1, 4, 1, 5, 9, 2, 6])
    assert result.lo == 1
    assert result.hi == 9


def test_single_value():
    result = ex.min_max([7])
    assert result == ex.MinMax(7, 7)


def test_empty_raises():
    with pytest.raises(ValueError):
        ex.min_max([])


def test_negative_values():
    result = ex.min_max([-3, -10, -1])
    assert result.lo == -10
    assert result.hi == -1


def test_returns_minmax_instance():
    assert isinstance(ex.min_max([1, 2]), ex.MinMax)


def test_unpacks_like_tuple():
    lo, hi = ex.min_max([5, 9, 2])
    assert (lo, hi) == (2, 9)
