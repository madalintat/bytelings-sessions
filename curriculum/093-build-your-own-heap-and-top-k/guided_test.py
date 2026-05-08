"""Tests for rung 3."""
import importlib.util
import random
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    h = ex.MinHeap()
    assert len(h) == 0
    assert bool(h) is False


def test_pop_empty_raises():
    h = ex.MinHeap()
    with pytest.raises(IndexError):
        h.pop()


def test_push_one_then_peek():
    h = ex.MinHeap()
    h.push(5)
    assert h.peek() == 5
    assert len(h) == 1


def test_push_then_sorted_pops():
    h = ex.MinHeap()
    for x in [5, 1, 3, 7, 2]:
        h.push(x)
    out = [h.pop() for _ in range(5)]
    assert out == [1, 2, 3, 5, 7]


def test_heapify_then_sorted_pops():
    h = ex.MinHeap([5, 1, 3, 7, 2, 9, 4])
    out = [h.pop() for _ in range(7)]
    assert out == [1, 2, 3, 4, 5, 7, 9]


def test_invariant_after_random_pushes():
    rnd = random.Random(0)
    h = ex.MinHeap()
    for _ in range(200):
        h.push(rnd.randint(-1000, 1000))
    # Pop everything; should come out in sorted order.
    out = [h.pop() for _ in range(200)]
    assert out == sorted(out)


def test_heapify_random():
    rnd = random.Random(1)
    items = [rnd.randint(-1000, 1000) for _ in range(200)]
    h = ex.MinHeap(items)
    out = [h.pop() for _ in range(200)]
    assert out == sorted(items)


def test_negative_values():
    h = ex.MinHeap([-3, 1, -10, 5, 0])
    assert h.peek() == -10


def test_duplicates_kept():
    h = ex.MinHeap([3, 3, 3])
    out = [h.pop(), h.pop(), h.pop()]
    assert out == [3, 3, 3]
