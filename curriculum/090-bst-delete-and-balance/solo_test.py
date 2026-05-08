"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _build(values):
    root = None

    def ins(node, x):
        if node is None:
            return ex._Node(x)
        if x < node.value:
            node.left = ins(node.left, x)
        elif x > node.value:
            node.right = ins(node.right, x)
        return node

    for v in values:
        root = ins(root, v)
    return root


def test_first():
    root = _build([5, 3, 7, 1, 4, 6, 8])
    assert ex.kth_smallest(root, 1) == 1


def test_last():
    root = _build([5, 3, 7, 1, 4, 6, 8])
    assert ex.kth_smallest(root, 7) == 8


def test_middle():
    root = _build([5, 3, 7, 1, 4, 6, 8])
    assert ex.kth_smallest(root, 4) == 5


def test_single_node():
    root = _build([42])
    assert ex.kth_smallest(root, 1) == 42


def test_k_zero_raises():
    root = _build([5, 3, 7])
    with pytest.raises(IndexError):
        ex.kth_smallest(root, 0)


def test_k_too_large_raises():
    root = _build([5, 3, 7])
    with pytest.raises(IndexError):
        ex.kth_smallest(root, 4)


def test_empty_raises():
    with pytest.raises(IndexError):
        ex.kth_smallest(None, 1)
