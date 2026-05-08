"""HIDDEN tests for rung 4."""
import importlib.util
import random
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    rs = ex.RangeSum([3, 1, 4, 1, 5, 9, 2])
    assert rs.query(0, 3) == 8
    assert rs.query(2, 5) == 10
    assert rs.query(0, 7) == 25
    assert rs.query(3, 3) == 0


def test_empty_array():
    rs = ex.RangeSum([])
    assert rs.query(0, 0) == 0


def test_single():
    rs = ex.RangeSum([42])
    assert rs.query(0, 1) == 42
    assert rs.query(1, 1) == 0


def test_negatives():
    rs = ex.RangeSum([-1, 2, -3, 4, -5])
    assert rs.query(0, 5) == -3
    assert rs.query(1, 4) == 3


def test_many_queries():
    random.seed(0)
    arr = [random.randint(-100, 100) for _ in range(500)]
    rs = ex.RangeSum(arr)
    for _ in range(200):
        a = random.randint(0, len(arr))
        b = random.randint(a, len(arr))
        assert rs.query(a, b) == sum(arr[a:b])
