"""Rung 2: Fluency drill — solved version.

size: base case for None is 0 (not 1), so the recursive 1 + ... counts
only real nodes.
height: base case for None is -1 (edges convention), giving height 0
for a leaf and -1 for an empty tree.
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
    """Return the total number of nodes in the tree."""
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)


def height(root: Optional[TreeNode]) -> int:
    """Return the height of the tree, measured in EDGES."""
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))
