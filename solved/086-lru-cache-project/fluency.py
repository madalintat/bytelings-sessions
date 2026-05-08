"""Rung 2: Fluency drill — solved version.

touch: move_to_end with last=False puts the key at the FRONT (MRU end).
evict_one: popitem(last=True) drops the BACK (LRU end).
"""
from collections import OrderedDict


def touch(cache: OrderedDict, key) -> None:
    """Mark `key` as most-recently-used inside `cache`."""
    if key in cache:
        cache.move_to_end(key, last=False)


def evict_one(cache: OrderedDict) -> None:
    """Remove the least-recently-used entry from `cache`."""
    if cache:
        cache.popitem(last=True)
