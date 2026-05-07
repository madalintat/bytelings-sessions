"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_new_stack_is_empty():
    s = ex.Stack()
    assert len(s) == 0
    assert bool(s) is False


def test_push_then_len():
    s = ex.Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert len(s) == 3


def test_peek_does_not_remove():
    s = ex.Stack()
    s.push("a")
    s.push("b")
    assert s.peek() == "b"
    assert len(s) == 2


def test_pop_lifo_order():
    s = ex.Stack()
    for x in [1, 2, 3]:
        s.push(x)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert len(s) == 0


def test_pop_empty_raises():
    s = ex.Stack()
    with pytest.raises(IndexError):
        s.pop()


def test_peek_empty_raises():
    s = ex.Stack()
    with pytest.raises(IndexError):
        s.peek()


def test_bool_truthy_when_nonempty():
    s = ex.Stack()
    s.push(0)  # even falsy values count as "in the stack"
    assert bool(s) is True
