"""Rung 2: Fluency — solved version.

The BST invariant is `left < node < right`. To INSERT, when x is
smaller than the current node we recurse LEFT; when larger, RIGHT.
The starter had the comparisons swapped (or absent), which would
either rebuild the tree wrong or loop forever.

Tail-recursion via reassignment is fine for a teaching example; for
production trees with depth >1000 you'd switch to an iterative loop
to avoid Python's recursion limit.
"""
from typing import Optional


class TreeNode:
    __slots__ = ("value", "left", "right")

    def __init__(self, value, left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.value = value
        self.left = left
        self.right = right


def bst_insert(root: Optional[TreeNode], x) -> TreeNode:
    """Insert x into the BST rooted at `root`. Return the (possibly new) root."""
    if root is None:
        return TreeNode(x)
    if x < root.value:
        root.left = bst_insert(root.left, x)
    elif x > root.value:
        root.right = bst_insert(root.right, x)
    return root
