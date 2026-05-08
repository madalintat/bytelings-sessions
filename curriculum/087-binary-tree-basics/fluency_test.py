"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_size_empty():
    assert ex.size(None) == 0


def test_size_leaf():
    assert ex.size(ex.TreeNode(1)) == 1


def test_size_three_node_tree():
    t = ex.TreeNode(1, ex.TreeNode(2), ex.TreeNode(3))
    assert ex.size(t) == 3


def test_size_skewed():
    t = ex.TreeNode(1, ex.TreeNode(2, ex.TreeNode(3)))
    assert ex.size(t) == 3


def test_height_none():
    assert ex.height(None) == -1


def test_height_leaf():
    assert ex.height(ex.TreeNode(1)) == 0


def test_height_balanced_three():
    t = ex.TreeNode(1, ex.TreeNode(2), ex.TreeNode(3))
    assert ex.height(t) == 1


def test_height_skewed():
    t = ex.TreeNode(1, ex.TreeNode(2, ex.TreeNode(3)))
    assert ex.height(t) == 2
