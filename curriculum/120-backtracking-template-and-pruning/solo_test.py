"""HIDDEN tests for rung 4."""
import importlib.util
import math
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _norm(out):
    return sorted(tuple(c) for c in out)


def test_basic():
    out = _norm(ex.combinations(4, 2))
    assert out == [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]


def test_k_zero():
    assert ex.combinations(5, 0) == [[]]


def test_k_eq_n():
    assert ex.combinations(3, 3) == [[1, 2, 3]]


def test_k_one():
    out = _norm(ex.combinations(3, 1))
    assert out == [(1,), (2,), (3,)]


def test_count_matches_n_choose_k():
    n, k = 6, 3
    assert len(ex.combinations(n, k)) == math.comb(n, k)


def test_each_is_sorted_ascending():
    out = ex.combinations(5, 3)
    for c in out:
        assert c == sorted(c)


def test_n_zero():
    assert ex.combinations(0, 0) == [[]]
