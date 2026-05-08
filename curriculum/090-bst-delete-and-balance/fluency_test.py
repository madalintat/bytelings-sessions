"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
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


def _inorder(node):
    if node is None:
        return []
    return _inorder(node.left) + [node.value] + _inorder(node.right)


def test_min_node_root_only():
    root = ex._Node(5)
    assert ex.min_node(root).value == 5


def test_min_node_finds_smallest():
    root = _build([5, 3, 7, 1, 4, 6, 8])
    assert ex.min_node(root).value == 1


def test_min_node_in_subtree():
    root = _build([5, 3, 7, 6, 8])
    assert ex.min_node(root.right).value == 6


def test_remove_leaf_simple():
    root = _build([5, 3, 7])
    root = ex.remove_leaf(root, 3)
    assert _inorder(root) == [5, 7]


def test_remove_leaf_deep():
    root = _build([5, 3, 7, 1, 4, 6, 8])
    root = ex.remove_leaf(root, 1)
    assert _inorder(root) == [3, 4, 5, 6, 7, 8]


def test_remove_leaf_keeps_others():
    root = _build([5, 3, 7])
    root = ex.remove_leaf(root, 7)
    assert _inorder(root) == [3, 5]
