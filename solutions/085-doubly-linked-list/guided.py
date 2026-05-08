"""Rung 3: Guided implement — a full DoublyLinkedList.

Topic: head + tail pointers, O(1) operations on both ends, O(1) delete-by-node.
"""
from typing import Iterator, Optional


class Node:
    __slots__ = ("value", "prev", "next")

    def __init__(self, value):
        self.value = value
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class DoublyLinkedList:
    """A doubly linked list with O(1) operations at both ends and O(1)
    delete-by-node.

    >>> dl = DoublyLinkedList()
    >>> dl.append(1); dl.append(2); dl.append(3)
    >>> list(dl)
    [1, 2, 3]
    >>> dl.prepend(0)
    >>> list(dl)
    [0, 1, 2, 3]
    >>> dl.pop_back()
    3
    >>> dl.pop_front()
    0
    >>> len(dl)
    2
    """

    def __init__(self) -> None:
        # TODO: head, tail, size.
        raise NotImplementedError

    def append(self, x) -> Node:
        """Add x at the tail. Return the new node so the caller can hold it
        for O(1) delete later.
        """
        # TODO: handle empty case (head/tail both become the new node).
        raise NotImplementedError

    def prepend(self, x) -> Node:
        """Add x at the head. Return the new node."""
        # TODO
        raise NotImplementedError

    def pop_front(self):
        """Remove and return the head value. Raise IndexError if empty."""
        # TODO: don't forget to update head, possibly tail (if list goes empty).
        raise NotImplementedError

    def pop_back(self):
        """Remove and return the tail value. Raise IndexError if empty."""
        # TODO
        raise NotImplementedError

    def delete(self, node: Node) -> None:
        """Splice `node` out of this list in O(1). Caller must guarantee
        `node` actually belongs to this list — we don't verify.
        """
        # TODO: rewire prev/next around node, update head/tail if it was either,
        # then decrement size.
        raise NotImplementedError

    def __len__(self) -> int:
        # TODO
        raise NotImplementedError

    def __iter__(self) -> Iterator:
        # TODO: walk head -> tail, yield values
        raise NotImplementedError
