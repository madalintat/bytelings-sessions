"""Rung 4: Solo — 0/1 knapsack, 1-D rolling array.

Topic: optimize the 2-D knapsack table to a single row.

Hidden tests in solo_test.py — don't peek before solving.

Implement `knapsack_1d(items, capacity) -> int`.

Contract:
- Same problem and return value as knapsack_2d from rung 3.
- CONSTRAINT: use only a SINGLE 1-D dp array of length capacity + 1.

The key insight: when updating dp[w] for item i, you must read from
the PREVIOUS row (item i-1).  If you iterate w left-to-right you'd
overwrite values you still need.  So iterate w from capacity DOWN to
wi (right-to-left).  That way dp[w - wi] is still from the "before
taking item i" state when you use it.

Example:
    knapsack_1d([(1,1),(3,4),(4,5),(5,7)], 7)  → 9

Patterns: P-28 (memoize-recursive).
"""


def knapsack_1d(items: list[tuple[int, int]], capacity: int) -> int:
    """Return max value fitting within capacity using a 1-D dp array.

    Iterate capacity in REVERSE to avoid double-counting items.
    """
    raise NotImplementedError
