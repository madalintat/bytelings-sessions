"""Rung 3: Guided implement — solved version.

LinkedList with head pointer and size counter. prepend is O(1); append
walks to the end O(n). pop_front rewires head. __iter__ walks the chain.
"""
from typing import Iterator, Optional


class Node:
    __slots__ = ("value", "next")

    def __init__(self, value, next: Optional["Node"] = None):
        self.value = value
        self.next = next


class LinkedList:
    """A singly linked list with O(1) prepend and pop_front, O(n) append."""

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self._size: int = 0

    def prepend(self, x) -> None:
        """Insert x at the front. O(1)."""
        self.head = Node(x, self.head)
        self._size += 1

    def append(self, x) -> None:
        """Insert x at the end. O(n)."""
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
        self._size += 1

    def pop_front(self):
        """Remove and return the front value. Raise IndexError if empty."""
        if self.head is None:
            raise IndexError("pop from empty list")
        value = self.head.value
        self.head = self.head.next
        self._size -= 1
        return value

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator:
        cur = self.head
        while cur is not None:
            yield cur.value
            cur = cur.next

    def __contains__(self, x) -> bool:
        for v in self:
            if v == x:
                return True
        return False
