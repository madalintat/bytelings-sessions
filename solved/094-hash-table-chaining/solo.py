"""Rung 4: Solo — solved version.

HashSet is a set backed by chaining. Internally it stores a list of
slot lists (each slot holds the values that hash there). The structure
is identical to HashMap except each entry is just a value, not a pair.

add: no-op if already present (check bucket first), otherwise append
  and increment size. Resize when load factor exceeds threshold.

remove: walk the bucket; splice out the value, decrement size. Raise
  KeyError if not found.

discard: like remove but silently returns if not found.
"""
from typing import Iterator


class HashSet:
    INITIAL_CAPACITY = 8
    MAX_LOAD = 0.75

    def __init__(self) -> None:
        self._slots: list[list] = [[] for _ in range(self.INITIAL_CAPACITY)]
        self._size: int = 0

    def _bucket(self, x) -> list:
        return self._slots[hash(x) % len(self._slots)]

    def add(self, x) -> None:
        bucket = self._bucket(x)
        if x in bucket:
            return
        bucket.append(x)
        self._size += 1
        if self._size / len(self._slots) > self.MAX_LOAD:
            self._resize(len(self._slots) * 2)

    def remove(self, x) -> None:
        bucket = self._bucket(x)
        try:
            bucket.remove(x)
        except ValueError:
            raise KeyError(x)
        self._size -= 1

    def discard(self, x) -> None:
        bucket = self._bucket(x)
        if x in bucket:
            bucket.remove(x)
            self._size -= 1

    def __contains__(self, x) -> bool:
        return x in self._bucket(x)

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator:
        for bucket in self._slots:
            yield from bucket

    def _resize(self, new_capacity: int) -> None:
        old_slots = self._slots
        self._slots = [[] for _ in range(new_capacity)]
        self._size = 0
        for bucket in old_slots:
            for x in bucket:
                self.add(x)
