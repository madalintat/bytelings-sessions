"""Rung 4: Solo implement — solved version.

move_to_front: if node is already the head, do nothing. Otherwise,
delete it (rewires its neighbors) and prepend it as the new head.
All O(1) — no list traversal.
"""
from typing import Iterator, Optional


class Node:
    __slots__ = ("value", "prev", "next")

    def __init__(self, value):
        self.value = value
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0

    def append(self, x) -> Node:
        n = Node(x)
        if self.tail is None:
            self.head = self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
        self._size += 1
        return n

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator:
        cur = self.head
        while cur is not None:
            yield cur.value
            cur = cur.next


def move_to_front(dl: DoublyLinkedList, node: Node) -> None:
    """Move `node` to be the head of `dl`. O(1)."""
    if node is dl.head:
        return
    # Splice node out.
    if node.prev is not None:
        node.prev.next = node.next
    if node.next is not None:
        node.next.prev = node.prev
    else:
        dl.tail = node.prev
    # Prepend node at head.
    node.prev = None
    node.next = dl.head
    if dl.head is not None:
        dl.head.prev = node
    dl.head = node
