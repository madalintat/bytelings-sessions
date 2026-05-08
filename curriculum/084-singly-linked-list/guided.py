"""Rung 3: Guided implement — a real LinkedList class.

Topic: the canonical singly-linked list with prepend/append/pop_front.
"""
from typing import Iterator, Optional


class Node:
    __slots__ = ("value", "next")

    def __init__(self, value, next: Optional["Node"] = None):
        self.value = value
        self.next = next


class LinkedList:
    """A singly linked list with O(1) prepend and pop_front, O(n) append.

    >>> ll = LinkedList()
    >>> ll.prepend(2); ll.prepend(1)
    >>> list(ll)
    [1, 2]
    >>> ll.append(3)
    >>> list(ll)
    [1, 2, 3]
    >>> ll.pop_front()
    1
    >>> len(ll)
    2
    """

    def __init__(self) -> None:
        # TODO: head and a size counter (so len() is O(1))
        raise NotImplementedError

    def prepend(self, x) -> None:
        """Insert x at the front. O(1)."""
        # TODO
        raise NotImplementedError

    def append(self, x) -> None:
        """Insert x at the end. O(n)."""
        # TODO: walk until cur.next is None, attach there
        raise NotImplementedError

    def pop_front(self):
        """Remove and return the front value. Raise IndexError if empty."""
        # TODO
        raise NotImplementedError

    def __len__(self) -> int:
        # TODO
        raise NotImplementedError

    def __iter__(self) -> Iterator:
        # TODO: walk from head, yield values
        raise NotImplementedError

    def __contains__(self, x) -> bool:
        # Default: walk and compare. We give you this one.
        for v in self:
            if v == x:
                return True
        return False
