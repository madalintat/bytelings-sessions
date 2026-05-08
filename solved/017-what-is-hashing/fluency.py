"""Rung 2: Fluency — solved version.

Three bugs in the Tiny hashmap:

  1. `[[]] * n` creates ONE list object aliased into every bucket slot.
     Appending to buckets[0] appends to all of them.
     Fix: `[[] for _ in range(n_buckets)]` — each `[]` is a new list.

  2. `hash(key)` without `% len(self.buckets)` can produce indices larger
     than the table size (and negative on some Python builds, causing
     IndexError). Fix: `hash(key) % len(self.buckets)`.

  3. The `get` method returns `bucket[0][1]` — the VALUE of the FIRST pair
     in the bucket, regardless of whether its key matches. Fix: walk the
     bucket and compare keys, exactly like `__contains__` does.
"""


class Tiny:
    def __init__(self, n_buckets: int = 8) -> None:
        self.buckets = [[] for _ in range(n_buckets)]

    def _bucket_for(self, key) -> list:
        return self.buckets[hash(key) % len(self.buckets)]

    def set(self, key, value) -> None:
        bucket = self._bucket_for(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key, default=None):
        for k, v in self._bucket_for(key):
            if k == key:
                return v
        return default

    def __contains__(self, key) -> bool:
        for k, _ in self._bucket_for(key):
            if k == key:
                return True
        return False
