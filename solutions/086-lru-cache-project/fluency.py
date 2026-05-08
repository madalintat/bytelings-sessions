"""Rung 2: Fluency drill — fix two LRU-cache helpers.

Topic: which end is "most recently used"?
"""
from collections import OrderedDict


def touch(cache: OrderedDict, key) -> None:
    """Mark `key` as most-recently-used inside `cache`. (No-op if not there.)

    By convention in this rung, the FRONT (left end) of the OrderedDict
    is the most-recently-used end. Use OrderedDict.move_to_end with
    last=False to move a key to the front.
    """
    # TODO: this moves to the WRONG end (the back) — fix it.
    if key in cache:
        cache.move_to_end(key, last=True)


def evict_one(cache: OrderedDict) -> None:
    """Remove the least-recently-used entry from `cache`.

    With "front = MRU", the LRU end is the BACK (right end). Use
    `popitem(last=True)` to drop it. No-op if the cache is empty.
    """
    # TODO: this drops the most-recent, not the oldest — fix it.
    if cache:
        cache.popitem(last=False)
