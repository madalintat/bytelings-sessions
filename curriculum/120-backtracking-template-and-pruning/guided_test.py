"""Tests for rung 3."""
import importlib.util
import math
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _norm(perms):
    return sorted(tuple(p) for p in perms)


def test_basic():
    out = _norm(ex.permutations([1, 2, 3]))
    expected = sorted([(1, 2, 3), (1, 3, 2), (2, 1, 3),
                       (2, 3, 1), (3, 1, 2), (3, 2, 1)])
    assert out == expected


def test_empty():
    assert ex.permutations([]) == [[]]


def test_single():
    assert ex.permutations([5]) == [[5]]


def test_count():
    """n elements → n! permutations."""
    n = 5
    assert len(ex.permutations(list(range(n)))) == math.factorial(n)


def test_strings():
    out = _norm(ex.permutations(["a", "b"]))
    assert out == sorted([("a", "b"), ("b", "a")])
