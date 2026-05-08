"""Rung 4: Solo — solved version.

kth_smallest uses an in-order traversal which visits BST nodes in
ascending order. We carry a mutable counter in a list (so the inner
function can decrement it) and raise StopIteration as a fast exit
once we hit the k-th element.

Using a generator + itertools.islice is an equivalent clean form:
stream the in-order values and pick the k-th one. Either approach is
O(h + k) where h is the tree height.
"""
from typing import Optional


class _Node:
    __slots__ = ("value", "left", "right")

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def kth_smallest(root: Optional[_Node], k: int):
    """Return the k-th smallest value (1-based). Raise IndexError if out of range."""
    if k <= 0:
        raise IndexError(f"k must be >= 1, got {k}")

    def inorder(node):
        if node is None:
            return
        yield from inorder(node.left)
        yield node.value
        yield from inorder(node.right)

    for i, val in enumerate(inorder(root), 1):
        if i == k:
            return val
    raise IndexError(f"k={k} is out of range")
