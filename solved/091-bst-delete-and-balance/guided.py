"""Rung 3: Guided — solved version.

delete uses the standard three-case recursive pattern:
  1. No children → return None (clears the parent's pointer).
  2. One child  → return that child (it splices up in place).
  3. Two children → copy the in-order successor's value into this
     node, then delete the successor from the right subtree. The
     successor has at most one child (no left child), so the recursive
     call hits case 1 or 2, not 3 again at that level.

height uses a simple post-order recursion: height of a subtree is
1 + max(height(left), height(right)), with the base case -1 for None
(edge-count convention: a single node has height 0).

is_skewed compares height to floor(log2(n)). A tree is skewed when
its height is more than 2 * ideal + 1, giving a small rounding
buffer for tiny trees.
"""
import math
from typing import Iterator, Optional


class _Node:
    __slots__ = ("value", "left", "right")

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    """Same shape as Day 89's BST, but with delete() and skew detection."""

    def __init__(self) -> None:
        self.root: Optional[_Node] = None
        self._size: int = 0

    def insert(self, x) -> None:
        def _ins(node):
            if node is None:
                self._size += 1
                return _Node(x)
            if x < node.value:
                node.left = _ins(node.left)
            elif x > node.value:
                node.right = _ins(node.right)
            return node

        self.root = _ins(self.root)

    def __contains__(self, x) -> bool:
        cur = self.root
        while cur is not None:
            if x == cur.value:
                return True
            cur = cur.left if x < cur.value else cur.right
        return False

    def __iter__(self) -> Iterator:
        def walk(n):
            if n is None:
                return
            yield from walk(n.left)
            yield n.value
            yield from walk(n.right)
        yield from walk(self.root)

    def __len__(self) -> int:
        return self._size

    def delete(self, x) -> bool:
        """Remove x. Return True if removed, False otherwise."""
        removed = [False]

        def _del(node):
            if node is None:
                return None
            if x < node.value:
                node.left = _del(node.left)
            elif x > node.value:
                node.right = _del(node.right)
            else:
                removed[0] = True
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                # Two children: replace value with in-order successor's,
                # then delete the successor from the right subtree.
                succ = node.right
                while succ.left is not None:
                    succ = succ.left
                node.value = succ.value
                node.right = _del(node.right)
                removed[0] = True  # ensure flag set even in recursive sub-call
            return node

        self.root = _del(self.root)
        if removed[0]:
            self._size -= 1
        return removed[0]

    def height(self) -> int:
        """Height in EDGES. Empty tree is -1; single node is 0."""
        def _h(node):
            if node is None:
                return -1
            return 1 + max(_h(node.left), _h(node.right))
        return _h(self.root)

    def is_skewed(self) -> bool:
        """True if height is more than 2 * floor(log2(n)) + 1."""
        n = self._size
        if n == 0:
            return False
        ideal = math.floor(math.log2(n))
        return self.height() > 2 * ideal + 1
