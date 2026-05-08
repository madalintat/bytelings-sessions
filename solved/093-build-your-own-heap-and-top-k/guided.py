"""Rung 3: Guided — solved version.

MinHeap is a 0-indexed min-heap backed by a plain Python list.

_sift_up: after appending a new item at the end, compare it with its
  parent. If it is smaller, swap and continue upward until the heap
  invariant holds or the root is reached.

_sift_down: after placing the last item at index 0 (pop), compare
  the node to its SMALLER child. If the node is larger, swap down.
  The "smaller child" guard is essential: swapping with the larger
  child can violate the invariant from above.

__init__ with items runs Floyd's linear-time heapify: sift down each
  non-leaf node in reverse order. This is O(n), cheaper than pushing
  one by one (O(n log n)).
"""
from typing import Iterable


class MinHeap:
    """A 0-indexed min-heap.

    >>> h = MinHeap()
    >>> for x in [5, 1, 3, 7, 2]: h.push(x)
    >>> h.peek()
    1
    >>> [h.pop() for _ in range(len(h))]
    [1, 2, 3, 5, 7]
    """

    def __init__(self, items: Iterable = ()) -> None:
        self.data: list = list(items)
        # Floyd heapify: sift down from the last non-leaf upward.
        for i in range(len(self.data) // 2 - 1, -1, -1):
            self._sift_down(i)

    def push(self, x) -> None:
        """Add x. O(log n)."""
        self.data.append(x)
        self._sift_up(len(self.data) - 1)

    def pop(self):
        """Remove and return the smallest. O(log n). Raise IndexError if empty."""
        if not self.data:
            raise IndexError("pop from empty heap")
        if len(self.data) == 1:
            return self.data.pop()
        top = self.data[0]
        self.data[0] = self.data.pop()
        self._sift_down(0)
        return top

    def peek(self):
        if not self.data:
            raise IndexError("peek at empty heap")
        return self.data[0]

    def __len__(self) -> int:
        return len(self.data)

    def __bool__(self) -> bool:
        return len(self.data) > 0

    # ---- internals ----
    def _sift_up(self, i: int) -> None:
        while i > 0:
            parent = (i - 1) // 2
            if self.data[i] < self.data[parent]:
                self.data[i], self.data[parent] = self.data[parent], self.data[i]
                i = parent
            else:
                break

    def _sift_down(self, i: int) -> None:
        n = len(self.data)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < n and self.data[left] < self.data[smallest]:
                smallest = left
            if right < n and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == i:
                break
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest
