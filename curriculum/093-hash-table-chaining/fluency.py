"""Rung 2: Fluency drill — fix the index math and the bucket lookup.

Topic: hash() % size, linear walk in a bucket.
"""


def bucket_index(key, size: int) -> int:
    """Return the bucket index for `key` in a table of `size` slots.

    Python's hash() can be NEGATIVE. Modding a negative by a positive
    in Python actually returns a non-negative result already (Python
    rounds toward -inf), so the simple expression works — but the
    magnitude must be the absolute hash value, not negation, for
    determinism. The implementation: hash(key) % size.
    """
    # TODO: this divides instead of mods, so the result is huge.
    return hash(key) // size


def find_in_bucket(bucket: list, key):
    """Return the value associated with `key` in the bucket (a list of
    (key, value) pairs), or None if not present.
    """
    # TODO: this returns the FIRST value regardless of key.
    if not bucket:
        return None
    return bucket[0][1]
