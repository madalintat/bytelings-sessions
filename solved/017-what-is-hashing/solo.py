"""Rung 4: Solo — solved version.

`TinySet` mirrors the `Tiny` hashmap but stores only keys (no values).
The API is `add`, `discard`, `__contains__`, `__len__`.

Implementation details:
  - `_size` tracks the count for O(1) len().
  - `add` scans the bucket; if the key is already present, it's a no-op
    (idempotent). Otherwise append and increment _size.
  - `discard` scans the bucket; if found, pop and decrement _size. No
    error if missing (unlike `remove` which would raise).
  - `__contains__` scans the bucket for the key.

The test bans using Python's built-in `set` or `dict` for storage
(checked by source inspection), so we use a list of bucket lists.
"""


class TinySet:
    def __init__(self, n_buckets: int = 8) -> None:
        self._buckets: list[list] = [[] for _ in range(n_buckets)]
        self._size: int = 0

    def _bucket_for(self, x) -> list:
        return self._buckets[hash(x) % len(self._buckets)]

    def add(self, x) -> None:
        bucket = self._bucket_for(x)
        for item in bucket:
            if item == x:
                return
        bucket.append(x)
        self._size += 1

    def discard(self, x) -> None:
        bucket = self._bucket_for(x)
        for i, item in enumerate(bucket):
            if item == x:
                bucket.pop(i)
                self._size -= 1
                return

    def __contains__(self, x) -> bool:
        for item in self._bucket_for(x):
            if item == x:
                return True
        return False

    def __len__(self) -> int:
        return self._size
