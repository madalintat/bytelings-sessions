"""Rung 4: Solo implement.

Topic: write `range_query(root, lo, hi)` — every value v with lo <= v <= hi.

Given the root of a BST (with the same `_Node` shape: value/left/right —
or any object with those three attrs) and a [lo, hi] inclusive range,
return all values inside that range, in sorted (ascending) order.

Examples (using a BST built by inserting 5, 3, 7, 1, 4, 6, 8):
    range_query(root, 3, 6)  -> [3, 4, 5, 6]
    range_query(root, 0, 2)  -> [1]
    range_query(root, 9, 99) -> []
    range_query(None, 1, 5)  -> []

Naive: do an inorder traversal and filter — O(n).

The BST way (worth the extra thought):
    - if node is None: return
    - if node.value >  lo:  recurse left
    - if lo <= node.value <= hi: emit node.value
    - if node.value <  hi:  recurse right
This skips entire subtrees that can't contain anything in [lo, hi].

Either is fine for the tests. Use the second for O(k + log n)
expected time when the tree is balanced.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
from typing import Optional


class _Node:
    __slots__ = ("value", "left", "right")

    def __init__(self, value, left: Optional["_Node"] = None,
                 right: Optional["_Node"] = None):
        self.value = value
        self.left = left
        self.right = right


def range_query(root: Optional[_Node], lo, hi) -> list:
    raise NotImplementedError
