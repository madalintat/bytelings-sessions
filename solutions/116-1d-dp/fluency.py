"""Rung 2: Fluency drill — trace the knapsack DP table.

Topic: 0/1 knapsack — fill missing cells by hand.

Items: [(w=1, v=1), (w=3, v=4), (w=4, v=5), (w=5, v=7)]
Capacity: 7

The DP table has (n+1) rows (item index 0..n) and (W+1) columns
(capacity 0..W).  Row 0 is all zeros (no items).

A PARTIAL table is given below (row 0 and some of row 1).  Your job is
to write `fill_table(partial)` that fills in all missing cells and
returns the COMPLETE table as a list-of-lists.

Recurrence:
    dp[i][w] = dp[i-1][w]                          # skip item i
    dp[i][w] = max(dp[i][w], dp[i-1][w-wi] + vi)  # take item i (if wi <= w)

ITEMS = [(1, 1), (3, 4), (4, 5), (5, 7)]
The correct final cell dp[4][7] should be 9.

TODO: implement `fill_table(partial)` below.
"""

ITEMS = [(1, 1), (3, 4), (4, 5), (5, 7)]
CAPACITY = 7

# Partial table: rows 0..4, columns 0..7
# Row 0 is complete; rows 1-4 are all zeros (you fill them).
PARTIAL = [
    [0, 0, 0, 0, 0, 0, 0, 0],  # row 0: no items
    [0, 0, 0, 0, 0, 0, 0, 0],  # row 1: TODO
    [0, 0, 0, 0, 0, 0, 0, 0],  # row 2: TODO
    [0, 0, 0, 0, 0, 0, 0, 0],  # row 3: TODO
    [0, 0, 0, 0, 0, 0, 0, 0],  # row 4: TODO
]


def fill_table(partial: list[list[int]]) -> list[list[int]]:
    """Fill missing cells and return the complete DP table.

    Do NOT modify `partial` in place — work on a copy.
    The final cell dp[4][7] should equal 9.
    """
    # TODO: implement this function
    raise NotImplementedError
