"""Tests for rung 2."""
import importlib.util
from collections import deque
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_make_queue_preserves_order():
    q = ex.make_queue([1, 2, 3])
    assert isinstance(q, deque)
    assert list(q) == [1, 2, 3]


def test_dequeue_returns_front():
    q = deque([1, 2, 3])
    assert ex.dequeue(q) == 1
    assert list(q) == [2, 3]


def test_round_trip_fifo():
    q = ex.make_queue(["a", "b", "c"])
    assert ex.dequeue(q) == "a"
    assert ex.dequeue(q) == "b"
    assert ex.dequeue(q) == "c"
