"""Rung 4: Solo implement.

Topic: write `move_to_front(dl, node)` for a DoublyLinkedList.

Given a DoublyLinkedList `dl` and a node `node` already inside it,
move `node` to be the new head of the list. This is the splice
operation at the heart of an LRU cache: the most recently used item
moves to the front.

Requirements:
    - Must be O(1). No walking the list.
    - Must work whether `node` is currently the head, tail, or middle.
    - Must NOT create a new node; reuse `node`.

The DoublyLinkedList in this file uses the same Node shape as Day 85's
guided rung: `value`, `prev`, `next`, plus `head`, `tail`, `_size`.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
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
    raise NotImplementedError
