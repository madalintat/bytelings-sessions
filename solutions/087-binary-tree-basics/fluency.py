"""Rung 2: Fluency drill — fix two near-correct tree helpers.

Topic: TreeNode recursion, base cases, off-by-one heights.
"""
from typing import Optional


class TreeNode:
    __slots__ = ("value", "left", "right")

    def __init__(self, value, left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.value = value
        self.left = left
        self.right = right


def size(root: Optional[TreeNode]) -> int:
    """Return the total number of nodes in the tree.

    size(None) == 0
    size(leaf) == 1
    """
    # TODO: this counts the current node twice (once here, once in the
    # base case after recursion).
    if root is None:
        return 1
    return 1 + size(root.left) + size(root.right)


def height(root: Optional[TreeNode]) -> int:
    """Return the height of the tree, measured in EDGES.

    height(None)        == -1
    height(single node) == 0
    height(root with one child) == 1
    """
    # TODO: the base cases are wrong (should be -1 for None, not 0).
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))
