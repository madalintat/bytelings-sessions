"""Rung 3: Guided implement — solved version.

LRUCache combines a dict (key -> node) and a doubly linked list with
sentinel head/tail nodes. _add_to_front inserts between head and
head.next; _remove splices out a node. get and put maintain MRU order
and evict the tail.prev (the LRU) when over capacity.
"""
from typing import Optional


class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev: Optional["_Node"] = None
        self.next: Optional["_Node"] = None


class LRUCache:
    """Bounded least-recently-used cache."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.map: dict = {}
        self.head = _Node(None, None)
        self.tail = _Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_front(self, node: _Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node: _Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_front(self, node: _Node) -> None:
        self._remove(node)
        self._add_to_front(node)

    def get(self, key):
        if key not in self.map:
            return None
        node = self.map[key]
        self._move_to_front(node)
        return node.value

    def put(self, key, value) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._move_to_front(node)
            return
        if len(self.map) == self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]
        new_node = _Node(key, value)
        self._add_to_front(new_node)
        self.map[key] = new_node

    def __len__(self) -> int:
        return len(self.map)
