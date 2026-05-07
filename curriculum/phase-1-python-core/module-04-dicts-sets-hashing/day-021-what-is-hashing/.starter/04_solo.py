"""Rung 4: Solo implement.

Topic: a Tiny SET on the same hash-bucket idea

Implement TinySet with these methods:
    add(x)        — add x; idempotent
    discard(x)    — remove x if present; no error if missing
    __contains__  — for `x in s`
    __len__

Constraint: must be O(1) average for add/discard/contains. Use the
hash-bucket pattern from concept.md.

Don't use Python's built-in set or dict for storage. Use a list of
buckets, each bucket a list.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


class TinySet:
    def __init__(self, n_buckets: int = 8) -> None:
        raise NotImplementedError

    def add(self, x) -> None:
        raise NotImplementedError

    def discard(self, x) -> None:
        raise NotImplementedError

    def __contains__(self, x) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
