"""HIDDEN tests for rung 4."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _inorder(node):
    if node is None:
        return []
    return _inorder(node.left) + [node.value] + _inorder(node.right)


def test_same_shape_both_none():
    assert ex.same_shape(None, None) is True


def test_same_shape_one_none():
    assert ex.same_shape(None, ex.TreeNode(1)) is False
    assert ex.same_shape(ex.TreeNode(1), None) is False


def test_same_shape_values_ignored():
    a = ex.TreeNode(1, ex.TreeNode(2))
    b = ex.TreeNode(99, ex.TreeNode(0))
    assert ex.same_shape(a, b) is True


def test_same_shape_different_structure():
    a = ex.TreeNode(1, ex.TreeNode(2))
    b = ex.TreeNode(1, None, ex.TreeNode(2))
    assert ex.same_shape(a, b) is False


def test_same_shape_deep_match():
    a = ex.TreeNode(1, ex.TreeNode(2, ex.TreeNode(4)), ex.TreeNode(3))
    b = ex.TreeNode(9, ex.TreeNode(8, ex.TreeNode(7)), ex.TreeNode(6))
    assert ex.same_shape(a, b) is True


def test_mirror_none():
    assert ex.mirror(None) is None


def test_mirror_single():
    m = ex.mirror(ex.TreeNode(1))
    assert _inorder(m) == [1]


def test_mirror_balanced():
    #     1
    #    / \
    #   2   3
    t = ex.TreeNode(1, ex.TreeNode(2), ex.TreeNode(3))
    m = ex.mirror(t)
    # in-order of original: [2, 1, 3]; mirror in-order: [3, 1, 2]
    assert _inorder(m) == [3, 1, 2]


def test_mirror_skewed():
    #   1
    #  /
    # 2
    t = ex.TreeNode(1, ex.TreeNode(2))
    m = ex.mirror(t)
    # original in-order: [2, 1]; mirror in-order: [1, 2]
    assert _inorder(m) == [1, 2]
