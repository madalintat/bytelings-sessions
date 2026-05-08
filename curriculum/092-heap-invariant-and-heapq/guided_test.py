"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    pq = ex.PriorityQueue()
    assert len(pq) == 0
    assert bool(pq) is False


def test_pop_empty_raises():
    pq = ex.PriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()


def test_peek_empty_raises():
    pq = ex.PriorityQueue()
    with pytest.raises(IndexError):
        pq.peek()


def test_priority_order():
    pq = ex.PriorityQueue()
    pq.push("c", 3)
    pq.push("a", 1)
    pq.push("b", 2)
    assert pq.pop() == "a"
    assert pq.pop() == "b"
    assert pq.pop() == "c"


def test_tiebreak_is_fifo():
    pq = ex.PriorityQueue()
    pq.push("first", 1)
    pq.push("second", 1)
    pq.push("third", 1)
    assert pq.pop() == "first"
    assert pq.pop() == "second"
    assert pq.pop() == "third"


def test_peek_does_not_remove():
    pq = ex.PriorityQueue()
    pq.push("a", 1)
    pq.push("b", 2)
    assert pq.peek() == "a"
    assert len(pq) == 2


def test_items_can_be_unhashable_or_uncomparable():
    """Two dicts can't be compared with <, so the heap must rely on
    the (priority, counter) prefix, never reaching the item slot."""
    pq = ex.PriorityQueue()
    a = {"name": "alice"}
    b = {"name": "bob"}
    pq.push(a, 1)
    pq.push(b, 1)
    # Should not raise.
    assert pq.pop() is a
    assert pq.pop() is b


def test_len_decreases_on_pop():
    pq = ex.PriorityQueue()
    pq.push("x", 1)
    pq.push("y", 2)
    pq.pop()
    assert len(pq) == 1
