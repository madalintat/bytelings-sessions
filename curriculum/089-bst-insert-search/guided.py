"""Rung 3: Guided implement — a real BST class.

Topic: insert/contains/min/max/iter on a binary search tree, set semantics.
"""
from typing import Iterator, Optional


class _Node:
    __slots__ = ("value", "left", "right")

    def __init__(self, value, left: Optional["_Node"] = None,
                 right: Optional["_Node"] = None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    """A binary search tree with set semantics (no duplicates).

    Operations (average O(log n) on a balanced tree, O(n) worst case):
        insert(x)        - add x; ignore if already present
        contains(x)      - bool
        min(), max()     - smallest/largest value, or None if empty
        len(t), bool(t)
        iter(t)          - sorted ascending (in-order traversal)

    >>> t = BST()
    >>> for x in [5, 3, 7, 1, 4]: t.insert(x)
    >>> list(t)
    [1, 3, 4, 5, 7]
    >>> 4 in t
    True
    >>> t.min(), t.max()
    (1, 7)
    """

    def __init__(self) -> None:
        self.root: Optional[_Node] = None
        self._size: int = 0

    def insert(self, x) -> None:
        """Add x. If x already present, do nothing."""
        # TODO: walk like search; when you fall off, attach a new node.
        # Increment self._size only when you actually create a node.
        # Tip: use the "return the (possibly new) subtree root" pattern
        # we used in fluency.
        raise NotImplementedError

    def contains(self, x) -> bool:
        # TODO
        raise NotImplementedError

    def __contains__(self, x) -> bool:
        return self.contains(x)

    def min(self):
        """Return the smallest value, or None if empty."""
        # TODO: walk all the way left from the root.
        raise NotImplementedError

    def max(self):
        """Return the largest value, or None if empty."""
        # TODO: walk all the way right from the root.
        raise NotImplementedError

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return self._size > 0

    def __iter__(self) -> Iterator:
        # TODO: in-order traversal generator.
        raise NotImplementedError
