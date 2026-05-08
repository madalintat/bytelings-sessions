"""Rung 3: Guided implement — solved version.

Queue wraps a deque. enqueue appends to the right; dequeue poplefts.
peek returns _data[0] (the front). Empty operations raise clear errors.
"""
from collections import deque


class Queue:
    """A FIFO queue backed by collections.deque."""

    def __init__(self) -> None:
        self._data: deque = deque()

    def enqueue(self, x) -> None:
        self._data.append(x)

    def dequeue(self):
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self):
        if not self._data:
            raise IndexError("peek from empty queue")
        return self._data[0]

    def __len__(self) -> int:
        return len(self._data)

    def __bool__(self) -> bool:
        return len(self) > 0
