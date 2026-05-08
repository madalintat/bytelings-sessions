"""Rung 2: Fluency — solved version.

probe_next: the stub returns i + 1 without wrapping, so it falls off
  the end of the array when i == capacity - 1. Fix: return (i + 1) % capacity.

find_slot: the loop body does nothing to advance `i`, so it spins
  forever when the first slot is occupied. Add `i = probe_next(i, capacity)`
  at the bottom of the loop body so it walks forward.
"""

EMPTY = object()
TOMB = object()


def probe_next(i: int, capacity: int) -> int:
    """Return the next slot index after `i`, wrapping around at `capacity`."""
    return (i + 1) % capacity


def find_slot(slots: list, key) -> int:
    """Find the slot for `key`: either the matching slot or the first EMPTY."""
    capacity = len(slots)
    i = hash(key) % capacity
    while True:
        slot = slots[i]
        if slot is EMPTY:
            return i
        if slot is not TOMB and slot[0] == key:
            return i
        i = probe_next(i, capacity)
