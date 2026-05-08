"""Rung 3: Guided — solved version.

PriorityQueue stores (priority, counter, item) tuples. The counter
from itertools.count() is a monotonically increasing integer that
acts as a stable tiebreaker: two items with the same priority come
out in insertion (FIFO) order, because the earlier-inserted one has
a smaller counter. This also means the heap never has to compare
`item` itself, which would crash on unhashable or uncomparable types
like dicts.

  push   — heappush the (priority, counter, item) triple.
  pop    — heappop and return index-2 (the item).
  peek   — read self._heap[0][2] without removing.
"""
import heapq
import itertools
from typing import Any


class PriorityQueue:
    """A min-priority queue: lower priority value = comes out first.

    Two items with equal priority come out in insertion order (FIFO).

    >>> pq = PriorityQueue()
    >>> pq.push("low", 5)
    >>> pq.push("high", 1)
    >>> pq.push("mid_first", 3)
    >>> pq.push("mid_second", 3)
    >>> pq.pop()
    'high'
    >>> pq.pop()
    'mid_first'
    """

    def __init__(self) -> None:
        self._heap: list = []
        self._counter = itertools.count()

    def push(self, item: Any, priority) -> None:
        heapq.heappush(self._heap, (priority, next(self._counter), item))

    def pop(self) -> Any:
        if not self._heap:
            raise IndexError("pop from empty PriorityQueue")
        return heapq.heappop(self._heap)[2]

    def peek(self) -> Any:
        if not self._heap:
            raise IndexError("peek at empty PriorityQueue")
        return self._heap[0][2]

    def __len__(self) -> int:
        return len(self._heap)

    def __bool__(self) -> bool:
        return len(self) > 0
