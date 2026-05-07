"""Rung 3: Guided implement — a full HashMap with chaining.

Topic: hash table with collision-by-chaining and load-factor resize.
"""
from typing import Iterator


_MISSING = object()  # sentinel for "key not present"


class HashMap:
    """A dict-like hash map using chaining. Approximate dict's API.

    Operations (average O(1) when load factor is bounded):
        put(key, value)
        get(key) -> value          (raises KeyError if missing)
        pop(key) -> value          (raises KeyError if missing)
        len(m)
        key in m
        iter(m)                    yields keys

    On insert, when size / capacity > 0.75, double the capacity and
    re-hash every entry.

    >>> m = HashMap()
    >>> m.put("alice", 31); m.put("bob", 22)
    >>> m.get("alice")
    31
    >>> "bob" in m
    True
    >>> m.pop("alice")
    31
    >>> "alice" in m
    False
    """

    INITIAL_CAPACITY = 8
    MAX_LOAD = 0.75

    def __init__(self) -> None:
        self._slots: list[list] = [[] for _ in range(self.INITIAL_CAPACITY)]
        self._size: int = 0

    def _bucket(self, key) -> list:
        return self._slots[hash(key) % len(self._slots)]

    def put(self, key, value) -> None:
        # TODO:
        # - find bucket
        # - if key already in bucket: overwrite, return
        # - else: append (key, value); _size += 1; resize if over MAX_LOAD
        raise NotImplementedError

    def get(self, key):
        # TODO: walk the bucket, return the value if key matches.
        # Raise KeyError(key) if missing.
        raise NotImplementedError

    def pop(self, key):
        # TODO: walk the bucket; if found, pop the entry, _size -= 1,
        # return the value. KeyError if missing.
        raise NotImplementedError

    def __contains__(self, key) -> bool:
        # default fallback that uses get; you can override
        for k, _ in self._bucket(key):
            if k == key:
                return True
        return False

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator:
        for bucket in self._slots:
            for k, _ in bucket:
                yield k

    def _resize(self, new_capacity: int) -> None:
        # TODO: build a new list of empty buckets, walk all entries,
        # re-insert each into the new bucket array, then swap.
        raise NotImplementedError
