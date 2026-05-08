"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _inorder(node):
    if node is None:
        return []
    return _inorder(node.left) + [node.value] + _inorder(node.right)


def test_insert_into_empty():
    root = ex.bst_insert(None, 5)
    assert root.value == 5
    assert root.left is None and root.right is None


def test_insert_smaller_goes_left():
    root = ex.bst_insert(None, 5)
    root = ex.bst_insert(root, 3)
    assert root.left is not None and root.left.value == 3
    assert root.right is None


def test_insert_larger_goes_right():
    root = ex.bst_insert(None, 5)
    root = ex.bst_insert(root, 7)
    assert root.right is not None and root.right.value == 7


def test_insert_yields_sorted_inorder():
    root = None
    for x in [5, 3, 7, 1, 4, 6, 8]:
        root = ex.bst_insert(root, x)
    assert _inorder(root) == [1, 3, 4, 5, 6, 7, 8]


def test_contains_hit():
    root = None
    for x in [5, 3, 7, 1]:
        root = ex.bst_insert(root, x)
    assert ex.bst_contains(root, 7) is True
    assert ex.bst_contains(root, 1) is True


def test_contains_miss():
    root = None
    for x in [5, 3, 7]:
        root = ex.bst_insert(root, x)
    assert ex.bst_contains(root, 99) is False
    assert ex.bst_contains(root, 4) is False


def test_contains_empty():
    assert ex.bst_contains(None, 1) is False
