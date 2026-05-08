"""Rung 3: Guided — solved version.

HashMap uses chaining: each slot holds a list of (key, value) pairs.

put: walk the bucket; overwrite if key exists, otherwise append and
  increment size. After insert, check load factor and resize if needed.

get: walk the bucket; return the value on a match, raise KeyError if
  none found.

pop: walk the bucket; splice out the matching pair, decrement size,
  return the value. Raise KeyError if none found.

_resize: double the capacity, re-insert every live entry by hashing
  them into the new slot array.
"""
from typing import Iterator


_MISSING = object()


class HashMap:
    """A dict-like hash map using chaining.

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
        bucket = self._bucket(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1
        if self._size / len(self._slots) > self.MAX_LOAD:
            self._resize(len(self._slots) * 2)

    def get(self, key):
        for k, v in self._bucket(key):
            if k == key:
                return v
        raise KeyError(key)

    def pop(self, key):
        bucket = self._bucket(key)
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return v
        raise KeyError(key)

    def __contains__(self, key) -> bool:
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
        old_slots = self._slots
        self._slots = [[] for _ in range(new_capacity)]
        self._size = 0
        for bucket in old_slots:
            for k, v in bucket:
                self.put(k, v)
