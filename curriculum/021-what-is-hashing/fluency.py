"""Rung 2: Fluency drill — a toy hashmap.

Topic: hash + buckets
"""


class Tiny:
    def __init__(self, n_buckets: int = 8) -> None:
        # TODO: this creates ONE shared list aliased into every slot
        self.buckets = [[]] * n_buckets

    def _bucket_for(self, key) -> list:
        # TODO: missing the modulo — this would index out of range
        return self.buckets[hash(key)]

    def set(self, key, value) -> None:
        bucket = self._bucket_for(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key, default=None):
        # TODO: returns the first item's value regardless of key
        bucket = self._bucket_for(key)
        if bucket:
            return bucket[0][1]
        return default

    def __contains__(self, key) -> bool:
        for k, _ in self._bucket_for(key):
            if k == key:
                return True
        return False
