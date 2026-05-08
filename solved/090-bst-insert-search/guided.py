"""Rung 3: Guided — solved version.

Idiomatic BST class with set semantics. Iterative `insert` and
`contains` because Python's recursion limit and stack overhead don't
add value here. `__iter__` is recursive because in-order traversal
naturally expresses left-then-self-then-right; the depth is bounded
by tree height (log n on a balanced tree).

`min()` and `max()` walk to the extreme; on the BST property, the
leftmost node is the smallest and the rightmost is the largest.
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
    def __init__(self) -> None:
        self._root: Optional[_Node] = None
        self._size = 0

    def insert(self, x) -> None:
        if self._root is None:
            self._root = _Node(x)
            self._size += 1
            return
        node = self._root
        while True:
            if x == node.value:
                return  # duplicate ignored
            if x < node.value:
                if node.left is None:
                    node.left = _Node(x)
                    self._size += 1
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = _Node(x)
                    self._size += 1
                    return
                node = node.right

    def contains(self, x) -> bool:
        node = self._root
        while node is not None:
            if x == node.value:
                return True
            node = node.left if x < node.value else node.right
        return False

    def min(self):
        if self._root is None:
            return None
        node = self._root
        while node.left is not None:
            node = node.left
        return node.value

    def max(self):
        if self._root is None:
            return None
        node = self._root
        while node.right is not None:
            node = node.right
        return node.value

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return self._size > 0

    def __iter__(self) -> Iterator:
        def inorder(node: Optional[_Node]) -> Iterator:
            if node is None:
                return
            yield from inorder(node.left)
            yield node.value
            yield from inorder(node.right)
        yield from inorder(self._root)

    def __contains__(self, x) -> bool:
        return self.contains(x)
