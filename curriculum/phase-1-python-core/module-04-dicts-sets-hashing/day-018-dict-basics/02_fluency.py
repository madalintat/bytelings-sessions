"""Rung 2: Fluency drill — dict basics.

Topic: lookup, get, in, items
"""


def lookup(d: dict, key, default=None):
    """Return d[key] if key present, else `default` — never raise."""
    # TODO: this raises KeyError on a miss
    return d[key]


def has_key(d: dict, key) -> bool:
    """Return True iff `key` is in `d` — no exception, no .keys() call."""
    # TODO: walking d.keys() linearly defeats the dict's superpower
    return key in list(d.keys())


def total_values(d: dict[str, int]) -> int:
    """Return the sum of all values in `d`."""
    # TODO: iterating gives keys, not values
    total = 0
    for x in d:
        total += x
    return total


def to_pairs(d: dict) -> list[tuple]:
    """Return [(k, v), ...] in dict insertion order."""
    # TODO: items() is the right call
    return list(d.keys())
