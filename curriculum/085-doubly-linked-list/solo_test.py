"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_move_middle_to_front():
    dl = ex.DoublyLinkedList()
    dl.append(1)
    b = dl.append(2)
    dl.append(3)
    ex.move_to_front(dl, b)
    assert list(dl) == [2, 1, 3]


def test_move_tail_to_front():
    dl = ex.DoublyLinkedList()
    dl.append(1)
    dl.append(2)
    c = dl.append(3)
    ex.move_to_front(dl, c)
    assert list(dl) == [3, 1, 2]


def test_move_head_is_noop():
    dl = ex.DoublyLinkedList()
    a = dl.append(1)
    dl.append(2)
    dl.append(3)
    ex.move_to_front(dl, a)
    assert list(dl) == [1, 2, 3]


def test_size_unchanged():
    dl = ex.DoublyLinkedList()
    dl.append(1)
    b = dl.append(2)
    dl.append(3)
    ex.move_to_front(dl, b)
    assert len(dl) == 3


def test_head_and_tail_correct_after_move():
    dl = ex.DoublyLinkedList()
    dl.append(1)
    dl.append(2)
    c = dl.append(3)
    ex.move_to_front(dl, c)
    assert dl.head is c
    assert dl.tail.value == 2


def test_two_node_swap():
    dl = ex.DoublyLinkedList()
    dl.append(1)
    b = dl.append(2)
    ex.move_to_front(dl, b)
    assert list(dl) == [2, 1]
    assert dl.head is b
    assert dl.tail.value == 1
