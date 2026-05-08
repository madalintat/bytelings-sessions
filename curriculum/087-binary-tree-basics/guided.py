"""Rung 3: Guided implement — basic shape queries on a binary tree.

Topic: recursive tree functions, base cases, "two questions" pattern.
"""
from typing import Optional


class TreeNode:
    __slots__ = ("value", "left", "right")

    def __init__(self, value, left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.value = value
        self.left = left
        self.right = right


def count_leaves(root: Optional[TreeNode]) -> int:
    """Return the number of leaves (nodes with no children).

    count_leaves(None)              == 0
    count_leaves(TreeNode(1))       == 1
    count_leaves(perfect 3-node)    == 2  # the two children
    """
    # TODO: base case for None; base case for leaf; otherwise sum left+right.
    raise NotImplementedError


def max_value(root: Optional[TreeNode]) -> Optional[int]:
    """Return the maximum integer value in the tree, or None if empty.

    >>> max_value(None) is None
    True
    >>> max_value(TreeNode(7))
    7
    >>> max_value(TreeNode(1, TreeNode(8), TreeNode(3)))
    8
    """
    # TODO: base case None -> None; otherwise compare current with
    # left/right max (skip None children).
    raise NotImplementedError


def is_balanced(root: Optional[TreeNode]) -> bool:
    """Return True if the tree is height-balanced.

    "Height-balanced" here means: at every node, the heights of the
    left and right subtrees differ by at most 1. None is balanced.
    A single node is balanced.

    height(None) == -1, height(leaf) == 0 (same convention as rung 2).
    """
    # TODO: a clean implementation returns (balanced, height) from
    # one helper to avoid recomputing height. You can also implement
    # naively with two recursions.
    raise NotImplementedError
