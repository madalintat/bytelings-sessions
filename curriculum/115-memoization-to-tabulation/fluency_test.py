"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_zero():
    assert ex.climb_bottomup(0) == 1


def test_one():
    assert ex.climb_bottomup(1) == 1


def test_small():
    assert ex.climb_bottomup(2) == 2
    assert ex.climb_bottomup(5) == 8


def test_large_no_recursion_limit():
    """Bottom-up should handle n=10_000 without RecursionError."""
    n = 10_000
    assert ex.climb_bottomup(n) > 0


def test_matches_topdown():
    for n in [3, 7, 20, 30]:
        assert ex.climb_bottomup(n) == ex.climb_topdown(n)
