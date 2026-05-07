"""Rung 2: Fluency drill — fix the broken probe walks.

Topic: linear probing, wrap-around, tombstones.
"""

# Sentinels representing "never used" and "deleted (tombstone)".
EMPTY = object()
TOMB = object()


def probe_next(i: int, capacity: int) -> int:
    """Return the next slot index after `i`, wrapping around at `capacity`.

    For example, probe_next(3, 8) -> 4. probe_next(7, 8) -> 0.
    """
    # TODO: this falls off the end at i == capacity - 1.
    return i + 1


def find_slot(slots: list, key) -> int:
    """Find the slot index where `key` lives, or where it would go.

    `slots` is a parallel list where each entry is either:
        - EMPTY (never used)
        - TOMB  (deleted; can be reused on insert, but lookups must walk past)
        - (k, v) tuple

    Linear-probe starting at hash(key) % capacity. Stop when you hit
    an EMPTY slot (key isn't in the table) or a slot whose key matches.
    Walk past TOMB slots — they're not the key but the chain might
    continue beyond.

    Return the slot index. If key isn't found, return the index of
    the first EMPTY slot encountered.
    """
    capacity = len(slots)
    i = hash(key) % capacity
    while True:
        slot = slots[i]
        if slot is EMPTY:
            return i
        if slot is not TOMB and slot[0] == key:
            return i
        # TODO: walk to the next slot — the loop never advances `i`.
        pass
