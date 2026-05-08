"""Rung 2: Fluency drill — solved version.

make_queue must append to the RIGHT (deque default), not the left.
dequeue must popleft() to take from the FRONT (FIFO order).
"""
from collections import deque


def make_queue(items: list) -> deque:
    """Return a deque containing `items` in the same order, ready for FIFO use."""
    q: deque = deque()
    for item in items:
        q.append(item)
    return q


def dequeue(q: deque):
    """Remove and return the front (oldest) item of the queue."""
    return q.popleft()
