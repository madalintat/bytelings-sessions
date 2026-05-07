"""Rung 3: Guided implement — full BST delete + a "is the tree skewed?" check.

Topic: the three deletion cases, and detecting an O(n) BST.
"""
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
        before = self._size

        def _ins(node):
            nonlocal before
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
        """Remove x. Return True if x was present and removed; False otherwise.

        Three cases at the matching node:
            1. no children:  return None  (the parent's child slot is cleared)
            2. one child:    return that child  (it splices up)
            3. two children: copy in-order successor's value here,
                             then delete the successor from the right subtree.
        """
        # TODO: implement using the recursive "return new subtree root" pattern.
        # Decrement self._size by 1 if you actually removed a node.
        # Tip: track removed via a closure flag, since recursion can't
        # easily return both a node and a bool.
        raise NotImplementedError

    def height(self) -> int:
        """Height in EDGES. Empty tree is -1; single node is 0."""
        # TODO
        raise NotImplementedError

    def is_skewed(self) -> bool:
        """Heuristic: True if the tree is more than 2x the ideal height.

        For n nodes a balanced BST has height ~ floor(log2(n)). We say
        the tree is skewed if its height is more than 2 * that ideal
        + 1 (the +1 absorbs tiny trees where rounding makes it noisy).
        Empty tree: not skewed.
        """
        # TODO
        raise NotImplementedError
