"""Rung 3: Guided — solved version.

`delete` scans the bucket for the matching (k, v) pair and removes it
with `bucket.pop(i)` or a list-comprehension reassignment. Using
`enumerate` gives the index for `pop`.

`__len__` simply returns `self._size`, which is maintained by `set`
(increments on new keys) and `delete` (decrements on removal). The
`set` method already handles the "overwrite doesn't grow" case by
returning before `_size += 1` when an existing key is found.
"""


class Tiny:
    def __init__(self, n_buckets: int = 8) -> None:
        self.buckets = [[] for _ in range(n_buckets)]
        self._size = 0

    def _bucket_for(self, key) -> list:
        return self.buckets[hash(key) % len(self.buckets)]

    def set(self, key, value) -> None:
        bucket = self._bucket_for(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1

    def get(self, key, default=None):
        for k, v in self._bucket_for(key):
            if k == key:
                return v
        return default

    def delete(self, key) -> bool:
        """Remove `key` from the map. Return True if it was present, False otherwise."""
        bucket = self._bucket_for(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return True
        return False

    def __len__(self) -> int:
        """Return the number of stored key-value pairs."""
        return self._size
