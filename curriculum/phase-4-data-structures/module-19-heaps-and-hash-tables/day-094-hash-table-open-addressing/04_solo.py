"""Rung 4: Solo implement.

Topic: write `cluster_lengths(slots)` — measure linear-probing clusters.

Given a `slots` list (the internal array of an open-addressed hash
table) where entries are either:
    - the EMPTY sentinel (defined here)
    - the TOMB sentinel (defined here)
    - an (key, value) tuple
return a list of integers, one per *contiguous run of non-EMPTY slots*
(i.e. (key, value) AND TOMB count as "occupied" for clustering — that's
the whole point: tombstones still slow down probes).

Wrap-around matters: a run that crosses the end of the array is a
single cluster. So a slots list of length 8 with occupied indices
[7, 0, 1] has cluster lengths [3].

Examples:
    cluster_lengths([EMPTY] * 8)          -> []
    cluster_lengths([("a", 1)] * 8)       -> [8]   (one big cluster, wraps)
    cluster_lengths([("a", 1), EMPTY, ("b", 2), ("c", 3), EMPTY, EMPTY, EMPTY, EMPTY])
        -> [1, 2]
    cluster_lengths([EMPTY, ("a", 1), TOMB, ("b", 2), EMPTY, EMPTY, ("c", 3), ("d", 4)])
        -> [3, 3]    # last cluster wraps from index 6 through 1: c, d, a, but
                    # actually index 0 is EMPTY in this case so it doesn't wrap.
                    # Wait — let's redo: slots[0] EMPTY, [1] a, [2] TOMB, [3] b,
                    # [4] EMPTY, [5] EMPTY, [6] c, [7] d.  No wrap. -> [3, 2].
                    # The wrap example is below.
    cluster_lengths([("a", 1), ("b", 2), EMPTY, EMPTY, EMPTY, EMPTY, ("c", 3), ("d", 4)])
        -> [4]   # wraps: [6] [7] [0] [1]

Returned cluster lengths can be in any order.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""

EMPTY = object()
TOMB = object()


def cluster_lengths(slots: list) -> list[int]:
    raise NotImplementedError
