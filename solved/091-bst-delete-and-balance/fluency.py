"""Rung 2: Fluency — solved version.

Two bugs, two fixes:

min_node: walking RIGHT gives the MAXIMUM, not the minimum. The
  minimum in a BST is always reached by following LEFT pointers all
  the way down. Change `while cur.right` to `while cur.left` and
  update the body to follow `cur.left`.

remove_leaf: when we find the matching leaf, we must return None so
  the parent's child pointer is cleared. The stub returns `root`
  unchanged. Change `return root` in the `x == root.value` branch
  to `return None`.
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
    cur = root
    while cur.left is not None:
        cur = cur.left
    return cur


def remove_leaf(root: _Node, x) -> Optional[_Node]:
    """Remove the LEAF node with value x from a BST. Return the new root.

    Precondition: x is present in the tree, x is at a leaf node.
    """
    if root is None:
        return None
    if x == root.value:
        return None  # leaf: just drop it
    if x < root.value:
        root.left = remove_leaf(root.left, x)
    else:
        root.right = remove_leaf(root.right, x)
    return root
