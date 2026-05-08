"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _sample_tree():
    return ex.TreeNode(
        4,
        ex.TreeNode(2, ex.TreeNode(1), ex.TreeNode(3)),
        ex.TreeNode(6, None, ex.TreeNode(7)),
    )


def test_inorder_empty():
    assert ex.inorder(None) == []


def test_inorder_single():
    assert ex.inorder(ex.TreeNode(7)) == [7]


def test_inorder_bst_sorted():
    assert ex.inorder(_sample_tree()) == [1, 2, 3, 4, 6, 7]


def test_inorder_skewed_left():
    # 3 -> 2 -> 1 (skewed left)
    t = ex.TreeNode(3, ex.TreeNode(2, ex.TreeNode(1)))
    assert ex.inorder(t) == [1, 2, 3]


def test_levelorder_empty():
    assert ex.levelorder(None) == []


def test_levelorder_single():
    assert ex.levelorder(ex.TreeNode(7)) == [7]


def test_levelorder_full():
    assert ex.levelorder(_sample_tree()) == [4, 2, 6, 1, 3, 7]


def test_levels_empty():
    assert ex.levels(None) == []


def test_levels_single():
    assert ex.levels(ex.TreeNode(7)) == [[7]]


def test_levels_full():
    assert ex.levels(_sample_tree()) == [[4], [2, 6], [1, 3, 7]]


def test_levels_skewed():
    t = ex.TreeNode(1, ex.TreeNode(2, ex.TreeNode(3)))
    assert ex.levels(t) == [[1], [2], [3]]
