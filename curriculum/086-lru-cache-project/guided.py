"""Rung 3: Guided implement — an LRU cache from a dict + doubly linked list.

Topic: combine two data structures so all three core ops are O(1).

For this rung we'll write the LRU using a small embedded doubly-linked-list
implementation (so it's self-contained), but you could equally use the
DoublyLinkedList class from Day 85.
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
    """Bounded least-recently-used cache.

    Operations:
        get(key)        -> value or None       O(1)
        put(key, value) -> None                O(1) amortized
        len(cache)      -> count                O(1)

    A get() that hits marks the key as most-recently-used.
    A put() of a NEW key into a full cache evicts the LRU first.
    A put() of an EXISTING key updates the value and marks it MRU.

    For convenience we use sentinel head/tail nodes so internal splicing
    has no None-checks. head.next is the MRU; tail.prev is the LRU.

    >>> c = LRUCache(2)
    >>> c.put("a", 1); c.put("b", 2)
    >>> c.get("a")
    1
    >>> c.put("c", 3)   # evicts "b" (LRU after the get above)
    >>> c.get("b") is None
    True
    """

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.map: dict = {}
        # sentinel nodes — head <-> ... <-> tail
        self.head = _Node(None, None)
        self.tail = _Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    # ---- private list helpers ----
    def _add_to_front(self, node: _Node) -> None:
        # TODO: insert `node` between self.head and self.head.next
        raise NotImplementedError

    def _remove(self, node: _Node) -> None:
        # TODO: splice `node` out (rewire prev/next neighbors)
        raise NotImplementedError

    def _move_to_front(self, node: _Node) -> None:
        self._remove(node)
        self._add_to_front(node)

    # ---- public API ----
    def get(self, key):
        # TODO: if key not in self.map, return None.
        # Otherwise, move the node to the front and return its value.
        raise NotImplementedError

    def put(self, key, value) -> None:
        # TODO:
        # - if key already in map: update value, move to front.
        # - else: create node, prepend, store in map.
        #     if over capacity: drop tail.prev (the LRU) from map AND list.
        raise NotImplementedError

    def __len__(self) -> int:
        return len(self.map)
