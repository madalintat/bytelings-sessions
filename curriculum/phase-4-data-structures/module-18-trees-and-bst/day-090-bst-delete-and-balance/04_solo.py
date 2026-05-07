"""Rung 4: Solo implement.

Topic: write `kth_smallest(root, k)` — the k-th smallest value in a BST.

Given the root of a BST and 1-based integer k, return the k-th
smallest value in the tree. Raise IndexError if k is out of range
(k <= 0, or k > size).

Examples (BST built from inserting 5, 3, 7, 1, 4, 6, 8):
    kth_smallest(root, 1) -> 1
    kth_smallest(root, 4) -> 5
    kth_smallest(root, 7) -> 8
    kth_smallest(root, 8) -> raises IndexError
    kth_smallest(root, 0) -> raises IndexError

The clean approach: an in-order traversal yields values ascending.
Walk inorder, decrement k each visit; when k hits 0, you have the
answer. You can stop early — no need to traverse the whole tree.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
from typing import Optional


class _Node:
    __slots__ = ("value", "left", "right")

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def kth_smallest(root: Optional[_Node], k: int):
    raise NotImplementedError
