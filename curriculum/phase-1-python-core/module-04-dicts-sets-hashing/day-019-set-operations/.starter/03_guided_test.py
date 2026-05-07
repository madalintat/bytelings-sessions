"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_half():
    # |intersection|=2 ({2,3}), |union|=4 ({1,2,3,4}) => 0.5
    assert ex.jaccard({1, 2, 3}, {2, 3, 4}) == 0.5


def test_identical():
    assert ex.jaccard({1, 2}, {1, 2}) == 1.0


def test_disjoint():
    assert ex.jaccard({1, 2}, {3, 4}) == 0.0


def test_one_empty():
    assert ex.jaccard({1}, set()) == 0.0
    assert ex.jaccard(set(), {1}) == 0.0


def test_both_empty():
    assert ex.jaccard(set(), set()) == 1.0


def test_returns_float():
    out = ex.jaccard({1, 2}, {1, 2})
    assert isinstance(out, float)
