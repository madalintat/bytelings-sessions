"""Rung 3: Guided implement — solved version.

DoublyLinkedList with head/tail/size. append and prepend return the
new node so callers can hold it for O(1) delete later. delete rewires
four pointers and handles the head/tail boundary cases.
"""
from typing import Iterator, Optional


class Node:
    __slots__ = ("value", "prev", "next")

    def __init__(self, value):
        self.value = value
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class DoublyLinkedList:
    """A doubly linked list with O(1) operations at both ends."""

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0

    def append(self, x) -> Node:
        """Add x at the tail. Return the new node."""
        n = Node(x)
        if self.tail is None:
            self.head = self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
        self._size += 1
        return n

    def prepend(self, x) -> Node:
        """Add x at the head. Return the new node."""
        n = Node(x)
        if self.head is None:
            self.head = self.tail = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n
        self._size += 1
        return n

    def pop_front(self):
        """Remove and return the head value. Raise IndexError if empty."""
        if self.head is None:
            raise IndexError("pop from empty list")
        value = self.head.value
        self.delete(self.head)
        return value

    def pop_back(self):
        """Remove and return the tail value. Raise IndexError if empty."""
        if self.tail is None:
            raise IndexError("pop from empty list")
        value = self.tail.value
        self.delete(self.tail)
        return value

    def delete(self, node: Node) -> None:
        """Splice `node` out of this list in O(1)."""
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = node.next = None
        self._size -= 1

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator:
        cur = self.head
        while cur is not None:
            yield cur.value
            cur = cur.next
