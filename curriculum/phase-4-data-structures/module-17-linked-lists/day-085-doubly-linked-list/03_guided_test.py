"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    dl = ex.DoublyLinkedList()
    assert len(dl) == 0
    assert list(dl) == []


def test_append_basic():
    dl = ex.DoublyLinkedList()
    dl.append(1)
    dl.append(2)
    dl.append(3)
    assert list(dl) == [1, 2, 3]
    assert len(dl) == 3


def test_prepend_basic():
    dl = ex.DoublyLinkedList()
    dl.prepend(3)
    dl.prepend(2)
    dl.prepend(1)
    assert list(dl) == [1, 2, 3]


def test_pop_front_and_back():
    dl = ex.DoublyLinkedList()
    for x in [10, 20, 30]:
        dl.append(x)
    assert dl.pop_front() == 10
    assert dl.pop_back() == 30
    assert list(dl) == [20]


def test_pop_until_empty():
    dl = ex.DoublyLinkedList()
    dl.append(1)
    assert dl.pop_back() == 1
    assert len(dl) == 0
    with pytest.raises(IndexError):
        dl.pop_back()
    with pytest.raises(IndexError):
        dl.pop_front()


def test_delete_middle():
    dl = ex.DoublyLinkedList()
    a = dl.append(1)  # noqa: F841
    b = dl.append(2)
    c = dl.append(3)  # noqa: F841
    dl.delete(b)
    assert list(dl) == [1, 3]
    assert len(dl) == 2


def test_delete_head():
    dl = ex.DoublyLinkedList()
    a = dl.append(1)
    dl.append(2)
    dl.delete(a)
    assert list(dl) == [2]


def test_delete_tail():
    dl = ex.DoublyLinkedList()
    dl.append(1)
    b = dl.append(2)
    dl.delete(b)
    assert list(dl) == [1]


def test_delete_only_node():
    dl = ex.DoublyLinkedList()
    a = dl.append(42)
    dl.delete(a)
    assert list(dl) == []
    assert len(dl) == 0
