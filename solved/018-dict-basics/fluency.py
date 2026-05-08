"""Rung 2: Fluency — solved version.

Four dict basics bugs:
  1. lookup: `d[key]` raises KeyError on a miss. Use `d.get(key, default)`
     which returns the default without raising.
  2. has_key: `key in list(d.keys())` does a LINEAR scan of the keys list.
     The whole point of a dict is O(1) membership: `key in d` checks
     against the hash table directly, not through a list copy.
  3. total_values: iterating over `d` yields KEYS. Use `d.values()` to
     iterate over values, or `sum(d.values())` as a one-liner.
  4. to_pairs: `d.keys()` returns keys. `d.items()` returns (key, value) pairs.
"""


def lookup(d: dict, key, default=None):
    """Return d[key] if key present, else `default` — never raise."""
    return d.get(key, default)


def has_key(d: dict, key) -> bool:
    """Return True iff `key` is in `d` — no exception, no .keys() call."""
    return key in d


def total_values(d: dict[str, int]) -> int:
    """Return the sum of all values in `d`."""
    return sum(d.values())


def to_pairs(d: dict) -> list[tuple]:
    """Return [(k, v), ...] in dict insertion order."""
    return list(d.items())
