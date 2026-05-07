"""Rung 2: Fluency drill — fix the backwards comparisons.

Topic: BST invariant — left < node < right.
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
    """Insert x into the BST rooted at `root`. Return the (possibly new) root.

    Duplicates are ignored. The BST property: left < node < right.
    """
    if root is None:
        return TreeNode(x)
    # TODO: the comparisons are backwards.
    if x > root.value:
        root.left = bst_insert(root.left, x)
    elif x < root.value:
        root.right = bst_insert(root.right, x)
    return root


def bst_contains(root: Optional[TreeNode], x) -> bool:
    """Return True iff x is in the BST."""
    if root is None:
        return False
    if x == root.value:
        return True
    # TODO: same problem — search the wrong side.
    if x > root.value:
        return bst_contains(root.left, x)
    return bst_contains(root.right, x)
