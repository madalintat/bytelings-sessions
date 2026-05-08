"""Rung 2: Fluency — solved version.

bucket_index: the stub uses integer division (//), which produces a
  result in the range [0, hash(key)//size], far outside the slot
  array bounds. The correct operation is modulo (%). Python's `%`
  already returns a non-negative value for any hash, so no abs() is
  needed.

find_in_bucket: the stub returns `bucket[0][1]` — always the first
  pair regardless of key. Fix by walking the list and checking
  `k == key`.
"""


def bucket_index(key, size: int) -> int:
    """Return the bucket index for `key` in a table of `size` slots."""
    return hash(key) % size


def find_in_bucket(bucket: list, key):
    """Return the value for `key` in the bucket, or None if missing."""
    for k, v in bucket:
        if k == key:
            return v
    return None
