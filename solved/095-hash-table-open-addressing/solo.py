"""Rung 4: Solo — solved version.

cluster_lengths finds contiguous runs of non-EMPTY slots. TOMB counts
as occupied for clustering purposes because probes still pass through it.

The wrap-around edge case: a run that begins near the end of the array
and continues at the beginning is a single cluster. To handle this,
find the first EMPTY slot as a canonical starting point, then do one
linear scan modulo len(slots). We count runs directly.

Algorithm:
  1. Find any EMPTY slot to use as a break point.
  2. Walk all n positions from that offset (wrapping). When we enter
     a non-EMPTY stretch, start counting. When we exit it, record the
     length.
  3. If no EMPTY slot exists the whole array is one cluster.
"""

EMPTY = object()
TOMB = object()


def cluster_lengths(slots: list) -> list[int]:
    """Return a list of lengths of contiguous non-EMPTY runs (wrap-aware)."""
    n = len(slots)
    if n == 0:
        return []

    def is_occupied(i):
        return slots[i] is not EMPTY

    # Find the first EMPTY slot to use as a guaranteed break point.
    start = None
    for i in range(n):
        if not is_occupied(i):
            start = i
            break

    if start is None:
        # Entire array is occupied — one cluster of length n.
        return [n]

    lengths = []
    run = 0
    for step in range(n):
        i = (start + step) % n
        if is_occupied(i):
            run += 1
        else:
            if run > 0:
                lengths.append(run)
                run = 0
    if run > 0:
        lengths.append(run)
    return lengths
