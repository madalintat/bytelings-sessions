"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.right_view(None) == []


def test_single():
    assert ex.right_view(ex.TreeNode(1)) == [1]


def test_balanced():
    #     1
    #    / \
    #   2   3
    t = ex.TreeNode(1, ex.TreeNode(2), ex.TreeNode(3))
    assert ex.right_view(t) == [1, 3]


def test_left_only_skew():
    #   1
    #  /
    # 2
    t = ex.TreeNode(1, ex.TreeNode(2))
    assert ex.right_view(t) == [1, 2]


def test_full_example():
    #     1
    #    / \
    #   2   3
    #  / \   \
    # 4   5   6
    t = ex.TreeNode(
        1,
        ex.TreeNode(2, ex.TreeNode(4), ex.TreeNode(5)),
        ex.TreeNode(3, None, ex.TreeNode(6)),
    )
    assert ex.right_view(t) == [1, 3, 6]


def test_left_extends_below_right():
    #     1
    #    / \
    #   2   3
    #  /
    # 4
    # 4 is the rightmost on its level since 3 has no children.
    t = ex.TreeNode(
        1,
        ex.TreeNode(2, ex.TreeNode(4)),
        ex.TreeNode(3),
    )
    assert ex.right_view(t) == [1, 3, 4]
