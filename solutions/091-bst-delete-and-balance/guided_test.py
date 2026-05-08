"""Tests for rung 3."""
import importlib.util
import math
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _build(values):
    t = ex.BST()
    for v in values:
        t.insert(v)
    return t


def test_delete_missing_returns_false():
    t = _build([5, 3, 7])
    assert t.delete(99) is False
    assert list(t) == [3, 5, 7]


def test_delete_leaf():
    t = _build([5, 3, 7])
    assert t.delete(3) is True
    assert list(t) == [5, 7]
    assert len(t) == 2


def test_delete_one_child():
    #     5
    #    / \
    #   3   7
    #        \
    #         8
    t = _build([5, 3, 7, 8])
    assert t.delete(7) is True
    assert list(t) == [3, 5, 8]


def test_delete_two_children():
    t = _build([5, 3, 7, 1, 4, 6, 8])
    assert t.delete(5) is True   # in-order successor is 6
    assert list(t) == [1, 3, 4, 6, 7, 8]
    assert len(t) == 6


def test_delete_root_when_only_node():
    t = _build([42])
    assert t.delete(42) is True
    assert list(t) == []
    assert len(t) == 0


def test_delete_then_insert_again():
    t = _build([5, 3, 7])
    t.delete(3)
    t.insert(3)
    assert list(t) == [3, 5, 7]
    assert len(t) == 3


def test_height_empty():
    t = ex.BST()
    assert t.height() == -1


def test_height_single():
    t = _build([5])
    assert t.height() == 0


def test_height_balanced_three():
    t = _build([5, 3, 7])
    assert t.height() == 1


def test_height_skewed_chain():
    t = _build([1, 2, 3, 4, 5])
    assert t.height() == 4


def test_skewed_chain_is_flagged():
    t = _build([1, 2, 3, 4, 5, 6, 7, 8])
    assert t.is_skewed() is True


def test_balanced_is_not_flagged():
    # roughly balanced inserts
    t = _build([4, 2, 6, 1, 3, 5, 7])
    assert t.is_skewed() is False


def test_empty_not_skewed():
    t = ex.BST()
    assert t.is_skewed() is False
