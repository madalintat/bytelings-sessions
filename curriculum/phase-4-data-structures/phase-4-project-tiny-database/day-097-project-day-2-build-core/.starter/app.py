"""Tiny in-memory database — Day 2: build the core.

You'll fill in insert / get / delete / range_query so all the tests
in test.py go green. The shape of the table is up to you, as long
as the public API matches Day 1's design.

A small BST is provided below for your convenience. Use it for the
range index, or replace it with the one you built on Day 89.
"""
from typing import Iterator, Optional


# ----------------------------------------------------------------------
#  A small BST keyed by tuples (range_key, row_id) so duplicates are OK.
# ----------------------------------------------------------------------
class _BSTNode:
    __slots__ = ("value", "left", "right")

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class _BST:
    """Set-semantics BST over comparable tuples."""

    def __init__(self) -> None:
        self.root: Optional[_BSTNode] = None
        self._size: int = 0

    def insert(self, value) -> None:
        def _ins(n):
            if n is None:
                self._size += 1
                return _BSTNode(value)
            if value < n.value:
                n.left = _ins(n.left)
            elif value > n.value:
                n.right = _ins(n.right)
            return n
        self.root = _ins(self.root)

    def delete(self, value) -> bool:
        removed = [False]

        def _min(n):
            while n.left is not None:
                n = n.left
            return n

        def _del(n):
            if n is None:
                return None
            if value < n.value:
                n.left = _del(n.left)
            elif value > n.value:
                n.right = _del(n.right)
            else:
                removed[0] = True
                if n.left is None:
                    return n.right
                if n.right is None:
                    return n.left
                succ = _min(n.right)
                n.value = succ.value
                n.right = _del2(n.right, succ.value)
            return n

        # Helper that uses a different "value" — we re-use _del with a
        # closure trick by making a tiny local recursion.
        def _del2(n, target):
            if n is None:
                return None
            if target < n.value:
                n.left = _del2(n.left, target)
            elif target > n.value:
                n.right = _del2(n.right, target)
            else:
                if n.left is None:
                    return n.right
                if n.right is None:
                    return n.left
                succ = _min(n.right)
                n.value = succ.value
                n.right = _del2(n.right, succ.value)
            return n

        self.root = _del(self.root)
        if removed[0]:
            self._size -= 1
        return removed[0]

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


# ----------------------------------------------------------------------
#  The Table.
# ----------------------------------------------------------------------
class Table:
    """In-memory table with hash + range indices."""

    def __init__(self) -> None:
        self._next_id: int = 1
        self._by_id: dict[int, dict] = {}
        self._by_range: _BST = _BST()

    def insert(self, range_key: int, payload: dict) -> int:
        """Add a row; assign a fresh integer id; index in both structures.

        Returns the new id.
        """
        # TODO:
        # 1. compute the new id (pull self._next_id, then increment)
        # 2. build the row dict: {"id": ..., "range_key": ..., **payload}
        # 3. add to self._by_id under the new id
        # 4. insert (range_key, new_id) into self._by_range
        # 5. return the new id
        raise NotImplementedError

    def get(self, row_id: int) -> Optional[dict]:
        """Return the row dict, or None if no such id."""
        # TODO: O(1) dict lookup
        raise NotImplementedError

    def delete(self, row_id: int) -> bool:
        """Remove the row. Return True if removed; False if not present.

        IMPORTANT: must remove from BOTH indices.
        """
        # TODO:
        # 1. if row_id not in self._by_id: return False
        # 2. fetch range_key from the row
        # 3. del self._by_id[row_id]
        # 4. self._by_range.delete((range_key, row_id))
        # 5. return True
        raise NotImplementedError

    def range_query(self, lo: int, hi: int) -> list[dict]:
        """Return rows whose range_key is in [lo, hi], inclusive,
        sorted ascending by range_key.
        """
        # TODO:
        # walk self._by_range in order; for each (rk, rid) tuple,
        # if lo <= rk <= hi, append self._by_id[rid] to a list.
        # Return the list. (Inorder traversal already gives ascending
        # order, so no extra sort is needed.)
        #
        # Optimization (optional): you can skip whole subtrees by
        # using a BST-aware range scan, the way Day 89's solo rung
        # did. Either is acceptable.
        raise NotImplementedError

    def __len__(self) -> int:
        return len(self._by_id)
