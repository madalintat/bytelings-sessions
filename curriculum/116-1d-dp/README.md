---
day: 116-knapsack-dp-shines
phase: phase-5-algorithms
module: module-24-dp-greedy-backtracking
style: build-it
---
# Day 116 — 0/1 knapsack: when DP is the *first* lens to reach for

Day 115 showed you DP after greedy failed. Today's problem is one
where DP is the *first* tool to grab. Recognizing why is the lesson —
the implementation is the easy part.

## The problem

```
You have N items, each with a weight w_i and a value v_i. You have a
knapsack with capacity W. Pick a subset of items (each item taken at
most ONCE — the "0/1" part) that fits within W and MAXIMIZES total
value.
```

Example: items `[(w=1, v=1), (w=3, v=4), (w=4, v=5), (w=5, v=7)]`,
capacity `7`. Best subset: items 2 and 4 (`w=3+5=8`? no, over) →
items 2 and 3 (`w=3+4=7, v=4+5=9`). Pick the third item too? No,
weight already at capacity. Optimum: `9`.

## Why your first instinct says greedy

The natural greedy: sort items by *value-per-weight ratio*, take in
order. Item 4 has v/w = 1.4, item 3 has 1.25, item 2 has 1.33,
item 1 has 1.0. Greedy picks: item 4 (w=5, v=7), can't fit item 2 next
(would be 8), tries item 3 (would be 9, over), tries item 1 (w=6, v=8).
Greedy answer: **8**. But the true optimum is **9**.

Greedy fails because *0/1* makes the choice non-divisible. (For
*fractional* knapsack — where you can take 0.5 of an item — greedy
*does* work, see Day 119.)

## The DP recognition signal

State: "the best value achievable using the first `i` items with
remaining capacity `w`." Two choices at each item:

- **Skip item i**: best value is `dp[i-1][w]` — same `w`, one fewer item considered.
- **Take item i** (only if `w_i <= w`): `dp[i-1][w - w_i] + v_i`.

```
dp[i][w] = max(
    dp[i-1][w],                                # skip
    dp[i-1][w - w_i] + v_i if w_i <= w else 0  # take
)
```

This is the DP signal in three words: **same subproblem, two choices**.
Both branches reduce to `dp[i-1][...]` — the same shape, smaller `i`.
Subproblems clearly overlap (you'll trace `dp[2][3]` from many parents).

## What "DP shines" means

The implementation is mechanical:

```python
def knapsack(items: list[tuple[int, int]], capacity: int) -> int:
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w_i, v_i = items[i - 1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if w_i <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - w_i] + v_i)
    return dp[n][capacity]
```

O(n × capacity) time and space. The optimization to a single 1-D
array (since each row only reads the previous row) is a polish step
the rungs walk you through.

## What's "shining"

The reason DP is celebrated isn't elegance — it's that **the same
recurrence pattern recurs across hundreds of "find the best X"
problems**. Once you've written the knapsack DP, you've prepared
yourself for: longest common subsequence, edit distance, matrix
chain multiplication, partition equal subset sum, minimum path sum,
and a dozen others. They're all `dp[i][j] = combine(dp[i-1][j], dp[i][j-1], …)`.

## Today's exercises

- **Fluency**: trace the DP table for the example above by hand, fill
  the missing cells. The diagnose helper points at the cell where
  you took an item that didn't fit.
- **Guided**: implement the 2-D version using the recurrence above.
- **Solo**: optimize to a 1-D array. Constraint: only one row alive
  at a time.
- **Apply**: a small CLI that reads items + capacity from a file and
  prints both the optimum *and the chosen items* — backtracking
  through the DP table.

## Pattern Catalog

`bytelings patterns P-28` — memoize-recursive. The top-down form
of today's `dp[i][w]`.

## Why this lens, today

The problem has the three classic DP signals: (a) optimization (max
value), (b) state with discrete dimensions (item index, remaining
capacity), (c) overlapping subproblems. When all three line up, DP
is the lens. Don't write the brute-force first; write the recurrence.

## Now: open `fluency.py`
