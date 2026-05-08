"""Rung 3: Guided implement — a PriorityQueue with insertion-order tiebreak.

Topic: tuple-keyed heaps for priority + stability.
"""
import heapq
import itertools
from typing import Any


class PriorityQueue:
    """A min-priority queue: lower priority value = comes out first.

    Two items with equal priority come out in insertion order (FIFO),
    not arbitrary order. We achieve that by storing
        (priority, counter, item)
    in the heap, where counter increases on every push so it acts as
    the tiebreaker. The third position holds the actual item.

    Operations:
        push(item, priority)  - O(log n)
        pop() -> item         - O(log n), raises IndexError if empty
        peek() -> item        - O(1), raises IndexError if empty
        len(pq), bool(pq)

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
        # TODO: the underlying heap and a counter (use itertools.count())
        raise NotImplementedError

    def push(self, item: Any, priority) -> None:
        # TODO: heappush a (priority, counter, item) tuple.
        raise NotImplementedError

    def pop(self) -> Any:
        # TODO: heappop and return the item slot.
        raise NotImplementedError

    def peek(self) -> Any:
        # TODO: read index 0 (the heap top), return the item slot.
        raise NotImplementedError

    def __len__(self) -> int:
        # TODO
        raise NotImplementedError

    def __bool__(self) -> bool:
        return len(self) > 0
