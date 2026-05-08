"""Tests for rung 2."""
import importlib.util
from collections import deque
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_make_ring_evicts_oldest():
    r = ex.make_ring(3)
    for x in [1, 2, 3, 4, 5]:
        r.append(x)
    assert list(r) == [3, 4, 5]


def test_make_ring_maxlen_set():
    r = ex.make_ring(7)
    assert r.maxlen == 7


def test_left_extend_preserves_order():
    d = deque([10])
    ex.left_extend_in_order(d, [1, 2, 3])
    assert list(d) == [1, 2, 3, 10]


def test_left_extend_empty_input():
    d = deque([5])
    ex.left_extend_in_order(d, [])
    assert list(d) == [5]
