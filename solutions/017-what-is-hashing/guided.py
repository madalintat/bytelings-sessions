"""Rung 3: Guided implement.

Topic: a Tiny hashmap with .delete

Implement `Tiny.delete(self, key)` and `Tiny.__len__`.
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
        """Remove `key` from the map. Return True if it was present, False otherwise.

        On removal, decrement self._size by 1.

        >>> t = Tiny()
        >>> t.set('a', 1)
        >>> t.delete('a')
        True
        >>> t.delete('a')
        False
        >>> t.get('a') is None
        True
        """
        # TODO: find the (k, v) pair in the bucket, pop it, decrement size.
        raise NotImplementedError

    def __len__(self) -> int:
        """Return the number of stored key-value pairs.

        >>> t = Tiny()
        >>> len(t)
        0
        >>> t.set('a', 1); t.set('b', 2)
        >>> len(t)
        2
        """
        # TODO: return self._size
        raise NotImplementedError
