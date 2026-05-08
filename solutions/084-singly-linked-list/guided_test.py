"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty_list():
    ll = ex.LinkedList()
    assert len(ll) == 0
    assert list(ll) == []


def test_prepend_order():
    ll = ex.LinkedList()
    ll.prepend(3)
    ll.prepend(2)
    ll.prepend(1)
    assert list(ll) == [1, 2, 3]
    assert len(ll) == 3


def test_append_order():
    ll = ex.LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert list(ll) == [1, 2, 3]


def test_mixed_prepend_append():
    ll = ex.LinkedList()
    ll.append(2)
    ll.prepend(1)
    ll.append(3)
    assert list(ll) == [1, 2, 3]


def test_pop_front_basic():
    ll = ex.LinkedList()
    ll.append(1)
    ll.append(2)
    assert ll.pop_front() == 1
    assert list(ll) == [2]
    assert len(ll) == 1


def test_pop_front_empty_raises():
    ll = ex.LinkedList()
    with pytest.raises(IndexError):
        ll.pop_front()


def test_contains():
    ll = ex.LinkedList()
    for x in [1, 2, 3]:
        ll.append(x)
    assert 2 in ll
    assert 99 not in ll


def test_iterates_twice():
    ll = ex.LinkedList()
    for x in [1, 2, 3]:
        ll.append(x)
    assert list(ll) == [1, 2, 3]
    assert list(ll) == [1, 2, 3]
