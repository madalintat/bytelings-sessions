"""Rung 3: Guided — solved version.

HashMapOA uses linear probing with tombstones for deletion.

_probe: linear probe from hash(key) % capacity. Walk through TOMB
  slots without stopping. Stop at EMPTY (key absent) or a key match.

_probe_for_insert: like _probe but remembers the first tombstone slot
  encountered on the way. If key not found, return that tombstone
  index (reuse it) rather than the EMPTY slot. This prevents the
  table from filling with dead slots over time.

pop: set the matching slot to TOMB rather than EMPTY so that probes
  which passed through it remain valid (tombstone-chaining invariant).

_resize: collect all live entries, build a fresh EMPTY array, re-insert
  each. Tombstones disappear — they were only needed to preserve chains
  during the table's lifetime, not across rehashes.
"""
from typing import Iterator

EMPTY = object()
TOMB = object()


class HashMapOA:
    """Hash map with open addressing + linear probing.

    >>> m = HashMapOA()
    >>> m.put("alice", 31); m.put("bob", 22)
    >>> m.get("alice")
    31
    >>> m.pop("alice")
    31
    >>> "alice" in m
    False
    """

    INITIAL_CAPACITY = 8
    MAX_LOAD = 0.7

    def __init__(self) -> None:
        self._slots: list = [EMPTY] * self.INITIAL_CAPACITY
        self._size: int = 0

    def _capacity(self) -> int:
        return len(self._slots)

    def _probe(self, key) -> int:
        cap = self._capacity()
        i = hash(key) % cap
        while True:
            slot = self._slots[i]
            if slot is EMPTY:
                return i
            if slot is not TOMB and slot[0] == key:
                return i
            i = (i + 1) % cap

    def _probe_for_insert(self, key) -> int:
        cap = self._capacity()
        i = hash(key) % cap
        first_tomb = None
        while True:
            slot = self._slots[i]
            if slot is EMPTY:
                return first_tomb if first_tomb is not None else i
            if slot is TOMB:
                if first_tomb is None:
                    first_tomb = i
            elif slot[0] == key:
                return i
            i = (i + 1) % cap

    def put(self, key, value) -> None:
        idx = self._probe_for_insert(key)
        slot = self._slots[idx]
        if slot is not EMPTY and slot is not TOMB and slot[0] == key:
            self._slots[idx] = (key, value)
        else:
            self._slots[idx] = (key, value)
            self._size += 1
            if self._size / self._capacity() > self.MAX_LOAD:
                self._resize(self._capacity() * 2)

    def get(self, key):
        idx = self._probe(key)
        slot = self._slots[idx]
        if slot is EMPTY or slot is TOMB:
            raise KeyError(key)
        return slot[1]

    def pop(self, key):
        idx = self._probe(key)
        slot = self._slots[idx]
        if slot is EMPTY or slot is TOMB:
            raise KeyError(key)
        value = slot[1]
        self._slots[idx] = TOMB
        self._size -= 1
        return value

    def __contains__(self, key) -> bool:
        idx = self._probe(key)
        slot = self._slots[idx]
        return slot is not EMPTY and slot is not TOMB and slot[0] == key

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator:
        for slot in self._slots:
            if slot is not EMPTY and slot is not TOMB:
                yield slot[0]

    def _resize(self, new_capacity: int) -> None:
        entries = [(k, v) for slot in self._slots
                   if slot is not EMPTY and slot is not TOMB
                   for k, v in [slot]]
        self._slots = [EMPTY] * new_capacity
        self._size = 0
        for k, v in entries:
            self.put(k, v)
