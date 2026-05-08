"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _sample_tree():
    #         4
    #        / \
    #       2   6
    #      / \   \
    #     1   3   7
    return ex.TreeNode(
        4,
        ex.TreeNode(2, ex.TreeNode(1), ex.TreeNode(3)),
        ex.TreeNode(6, None, ex.TreeNode(7)),
    )


def test_preorder_empty():
    assert ex.preorder(None) == []


def test_preorder_single():
    assert ex.preorder(ex.TreeNode(7)) == [7]


def test_preorder_full():
    assert ex.preorder(_sample_tree()) == [4, 2, 1, 3, 6, 7]


def test_postorder_empty():
    assert ex.postorder(None) == []


def test_postorder_single():
    assert ex.postorder(ex.TreeNode(7)) == [7]


def test_postorder_full():
    assert ex.postorder(_sample_tree()) == [1, 3, 2, 7, 6, 4]
