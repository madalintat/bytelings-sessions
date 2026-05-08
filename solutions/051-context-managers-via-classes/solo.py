"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: a transactional in-memory store

Build `Transaction(store)`:
- `store` is a dict.
- On entry, snapshot the store's current contents.
- During the `with` block, the user may modify the store freely.
- On normal exit, leave the store as-is (commit).
- On exit due to any exception, restore the store to the snapshot
  (rollback) and let the exception propagate.

Usage:
    store = {"a": 1}
    try:
        with Transaction(store):
            store["b"] = 2
            raise RuntimeError("boom")
    except RuntimeError:
        pass
    # store is back to {"a": 1} — the "b" was rolled back

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


class Transaction:
    def __init__(self, store: dict) -> None:
        raise NotImplementedError
