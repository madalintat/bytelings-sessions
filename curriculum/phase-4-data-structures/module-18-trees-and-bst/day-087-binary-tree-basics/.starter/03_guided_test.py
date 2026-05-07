"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_leaves_empty():
    assert ex.count_leaves(None) == 0


def test_leaves_single():
    assert ex.count_leaves(ex.TreeNode(1)) == 1


def test_leaves_three_node():
    t = ex.TreeNode(1, ex.TreeNode(2), ex.TreeNode(3))
    assert ex.count_leaves(t) == 2


def test_leaves_skewed():
    t = ex.TreeNode(1, ex.TreeNode(2, ex.TreeNode(3)))
    assert ex.count_leaves(t) == 1


def test_leaves_complex():
    #         1
    #        / \
    #       2   3
    #      /     \
    #     4       5
    t = ex.TreeNode(1,
                    ex.TreeNode(2, ex.TreeNode(4)),
                    ex.TreeNode(3, None, ex.TreeNode(5)))
    assert ex.count_leaves(t) == 2


def test_max_empty():
    assert ex.max_value(None) is None


def test_max_single():
    assert ex.max_value(ex.TreeNode(7)) == 7


def test_max_basic():
    t = ex.TreeNode(1, ex.TreeNode(8), ex.TreeNode(3))
    assert ex.max_value(t) == 8


def test_max_with_negatives():
    t = ex.TreeNode(-1, ex.TreeNode(-5), ex.TreeNode(-3))
    assert ex.max_value(t) == -1


def test_balanced_empty():
    assert ex.is_balanced(None) is True


def test_balanced_single():
    assert ex.is_balanced(ex.TreeNode(1)) is True


def test_balanced_perfect():
    t = ex.TreeNode(1, ex.TreeNode(2), ex.TreeNode(3))
    assert ex.is_balanced(t) is True


def test_unbalanced_skewed():
    t = ex.TreeNode(1, ex.TreeNode(2, ex.TreeNode(3, ex.TreeNode(4))))
    assert ex.is_balanced(t) is False


def test_balanced_diff_by_one():
    #     1
    #    / \
    #   2   3
    #  /
    # 4
    t = ex.TreeNode(1,
                    ex.TreeNode(2, ex.TreeNode(4)),
                    ex.TreeNode(3))
    assert ex.is_balanced(t) is True
