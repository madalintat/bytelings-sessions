"""Rung 3: Guided implement — write a Queue class wrapping deque.

Topic: a real FIFO queue with O(1) enqueue and dequeue.
"""
from collections import deque


class Queue:
    """A FIFO queue backed by collections.deque.

    Operations:
        enqueue(x): add x to the back              O(1)
        dequeue():  remove and return the front    O(1)
        peek():     return the front, no remove    O(1)
        len(q):     number of items                O(1)
        bool(q):    False when empty               O(1)

    dequeue() and peek() raise IndexError on an empty queue with the
    message "<op> from empty queue".

    >>> q = Queue()
    >>> q.enqueue(1); q.enqueue(2)
    >>> q.peek()
    1
    >>> q.dequeue()
    1
    """

    def __init__(self) -> None:
        # TODO: use a deque
        raise NotImplementedError

    def enqueue(self, x) -> None:
        # TODO
        raise NotImplementedError

    def dequeue(self):
        # TODO: raise IndexError("dequeue from empty queue") when empty
        raise NotImplementedError

    def peek(self):
        # TODO: raise IndexError("peek from empty queue") when empty
        raise NotImplementedError

    def __len__(self) -> int:
        # TODO
        raise NotImplementedError

    def __bool__(self) -> bool:
        return len(self) > 0
