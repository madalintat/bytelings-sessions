"""Rung 2: Fluency drill — fix the misbehaving queue helpers.

Topic: deque vs list, the right end for FIFO.
"""
from collections import deque


def make_queue(items: list) -> deque:
    """Return a deque containing `items` in the same order, ready for FIFO use.

    enqueue at the right, dequeue from the left.
    """
    # TODO: this builds a deque, but in REVERSE order — fix it.
    q: deque = deque()
    for item in items:
        q.appendleft(item)
    return q


def dequeue(q: deque):
    """Remove and return the front (oldest) item of the queue."""
    # TODO: pop() removes from the WRONG end for a queue — fix it.
    return q.pop()
