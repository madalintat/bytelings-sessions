"""Rung 2: Fluency drill — fix the broken BST helpers.

Topic: deletion building blocks (min-node walk, leaf splice).
"""
from typing import Optional


class _Node:
    __slots__ = ("value", "left", "right")

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def min_node(root: _Node) -> _Node:
    """Return the node with the smallest value in this subtree.

    Precondition: root is not None.
    Walk left until you can't.
    """
    # TODO: this walks RIGHT (so it returns max). Fix it.
    cur = root
    while cur.right is not None:
        cur = cur.right
    return cur


def remove_leaf(root: _Node, x) -> Optional[_Node]:
    """Remove the LEAF node with value x from a BST. Return the new root.

    Precondition: x is present in the tree, x is at a leaf node.

    Walk the tree like a search; when we find the leaf, return None
    so the parent's child link gets cleared.
    """
    if root is None:
        return None
    # TODO: this returns root unchanged when x matches a leaf, instead
    # of returning None.
    if x == root.value:
        return root
    if x < root.value:
        root.left = remove_leaf(root.left, x)
    else:
        root.right = remove_leaf(root.right, x)
    return root
