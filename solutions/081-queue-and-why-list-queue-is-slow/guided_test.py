"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_new_queue_is_empty():
    q = ex.Queue()
    assert len(q) == 0
    assert bool(q) is False


def test_enqueue_then_len():
    q = ex.Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert len(q) == 2


def test_peek_returns_front_no_remove():
    q = ex.Queue()
    q.enqueue("a")
    q.enqueue("b")
    assert q.peek() == "a"
    assert len(q) == 2


def test_dequeue_fifo_order():
    q = ex.Queue()
    for x in [1, 2, 3]:
        q.enqueue(x)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert len(q) == 0


def test_dequeue_empty_raises():
    q = ex.Queue()
    with pytest.raises(IndexError):
        q.dequeue()


def test_peek_empty_raises():
    q = ex.Queue()
    with pytest.raises(IndexError):
        q.peek()


def test_bool_truthy_with_falsy_value():
    q = ex.Queue()
    q.enqueue(0)
    assert bool(q) is True
