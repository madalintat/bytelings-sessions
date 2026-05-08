"""Rung 3: Guided implement — open-addressed HashMapOA with tombstones.

Topic: linear probing, deletion via tombstones, resize on load.
"""
from typing import Iterator


# Sentinels.
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
    MAX_LOAD = 0.7   # lower than chaining; clusters slow probes

    def __init__(self) -> None:
        self._slots: list = [EMPTY] * self.INITIAL_CAPACITY
        self._size: int = 0   # live entries (not counting tombstones)

    def _capacity(self) -> int:
        return len(self._slots)

    def _probe(self, key) -> int:
        """Find the slot index for `key`, walking past TOMBs.
        Returns either the index of a matching key, or the first EMPTY slot.
        """
        # TODO: linear-probe from hash(key) % capacity, wrapping around.
        # Stop at a slot that is EMPTY, or whose key matches `key`.
        # Walk through TOMB slots without stopping.
        raise NotImplementedError

    def _probe_for_insert(self, key) -> int:
        """Like _probe, but on the way to finding the key (or empty slot),
        REMEMBER the FIRST tombstone we passed. Inserts can reuse it.

        Returns:
          - if key is already present: the index of the matching slot.
          - else: the index of the first TOMB encountered (if any),
                  or the EMPTY slot we eventually hit.
        """
        # TODO
        raise NotImplementedError

    def put(self, key, value) -> None:
        # TODO:
        # - find idx via _probe_for_insert
        # - if slot is a (k, v) match: overwrite value at slot
        # - else: store (key, value); _size += 1; resize if over MAX_LOAD
        raise NotImplementedError

    def get(self, key):
        # TODO: probe; if EMPTY, raise KeyError; else return value.
        raise NotImplementedError

    def pop(self, key):
        # TODO: probe; if EMPTY, raise KeyError; else read value,
        # set slot to TOMB, _size -= 1, return value.
        raise NotImplementedError

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
        # TODO: collect all live entries, allocate a fresh EMPTY array of
        # new_capacity, re-insert each via put-style logic. Tombstones
        # disappear in this pass.
        raise NotImplementedError
