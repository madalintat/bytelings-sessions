"""Rung 4: Solo — solved version.

`Transaction` snapshots the store dict on entry (`dict(store)` is a
shallow copy). On clean exit it does nothing — the mutations already
live in `store`. On exit due to an exception it restores the snapshot
by clearing the store and re-filling it, then returns `False` so the
exception propagates.
"""


class Transaction:
    def __init__(self, store: dict) -> None:
        self._store = store
        self._snapshot: dict | None = None

    def __enter__(self):
        self._snapshot = dict(self._store)
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type is not None:
            self._store.clear()
            self._store.update(self._snapshot)
        return False
