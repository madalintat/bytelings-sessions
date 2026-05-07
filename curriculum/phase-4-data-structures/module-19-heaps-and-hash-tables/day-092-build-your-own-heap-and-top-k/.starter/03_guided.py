"""Rung 3: Guided implement — a min-heap from scratch.

Topic: push/pop/peek/heapify in plain Python, no heapq.
"""
from typing import Iterable


class MinHeap:
    """A 0-indexed min-heap on top of a Python list.

    Invariant: for every i > 0, data[(i-1)//2] <= data[i].
    Therefore data[0] is always the minimum.

    >>> h = MinHeap()
    >>> for x in [5, 1, 3, 7, 2]: h.push(x)
    >>> h.peek()
    1
    >>> [h.pop() for _ in range(len(h))]
    [1, 2, 3, 5, 7]
    """

    def __init__(self, items: Iterable = ()) -> None:
        self.data: list = list(items)
        # Heapify: sift down each non-leaf in reverse, so the bottom of
        # the array is already a heap when we touch its parent.
        # TODO: implement (you'll need _sift_down below; you can leave
        # this as `for i in range(len(self.data)//2 - 1, -1, -1): self._sift_down(i)`).
        raise NotImplementedError

    def push(self, x) -> None:
        """Add x. O(log n)."""
        # TODO: append to data, then _sift_up the new last index.
        raise NotImplementedError

    def pop(self):
        """Remove and return the smallest. O(log n). Raise IndexError if empty."""
        # TODO:
        # - if empty: raise IndexError("pop from empty heap")
        # - if size 1: pop and return
        # - else: save data[0], move data[-1] to data[0], shrink, sift_down(0)
        raise NotImplementedError

    def peek(self):
        # TODO
        raise NotImplementedError

    def __len__(self) -> int:
        return len(self.data)

    def __bool__(self) -> bool:
        return len(self.data) > 0

    # ---- internals ----
    def _sift_up(self, i: int) -> None:
        # TODO
        raise NotImplementedError

    def _sift_down(self, i: int) -> None:
        # TODO: compare against the SMALLER child (mind the right-child trap).
        raise NotImplementedError
