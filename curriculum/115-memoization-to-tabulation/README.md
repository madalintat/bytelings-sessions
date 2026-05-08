---
day: day-115-memoization-to-tabulation
phase: phase-5-algorithms
module: module-24-dp-greedy-backtracking
style: tour
---
# Day 115 — A guided tour: same DP, two flavors

Yesterday you cached a recursion. That's **top-down DP**: start from
the answer you want, recurse to smaller subproblems, cache.

Today's tour visits the alternative: **bottom-up DP** (also called
tabulation). Same problem, same recurrence — opposite direction.

## Stop 1 — the top-down version (refresher)

```python
from functools import cache

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

You ask for `fib(40)`. The cache fills with answers in whatever order
the recursion stumbles into. By the time the top-level call returns,
every subproblem 0..40 is computed exactly once.

## Stop 2 — the same thing, bottom-up

```python
def fib(n):
    if n <= 1:
        return n
    table = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]
```

You **iterate**. You **fill a table** in dependency order. By the
time you reach index 40, you've explicitly computed 2, 3, ... 39
already. No recursion, no implicit cache.

This shape — a table indexed by problem size, filled in order — is
**tabulation**.

## Stop 3 — the trade-offs

| | Top-down (memoization) | Bottom-up (tabulation) |
|---|---|---|
| Code length | shorter | longer |
| Mental model | follow the recurrence | think about fill order |
| Stack | recursion depth (Python ≤ 1000) | none |
| Wasted work | computes only needed states | computes the whole table |
| Easy to "shrink memory" | hard | easy (often O(1) space) |
| Best when | recurrence is easy to state | full table will be filled anyway |

**Key insight:** for fib, almost every subproblem is needed, so
tabulation isn't wasteful. But for problems where you only touch a
small part of the state space, top-down is faster — it computes
exactly what's needed.

## Stop 4 — the space optimization that's hard top-down, easy bottom-up

Look back at the bottom-up `fib`. At iteration i, you only need
`table[i-1]` and `table[i-2]`. You don't need `table[0..i-3]` ever
again. So:

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

O(1) space. Two variables instead of a whole array. The bottom-up
version made this "rolling" optimization obvious; the top-down
version hides it.

This trick — keeping only the most recent slice of the table —
applies to most 1D DPs (next day) and even some 2D DPs (day after).

## Stop 5 — when each one wins in practice

- **Reach for top-down (`@cache`)** when the recurrence is the easy
  part. You write it the way you'd describe it on a whiteboard;
  Python handles the rest.
- **Reach for bottom-up** when:
  - Recursion depth would be a problem (long chains, like > 1000).
  - You want to space-optimize.
  - The fill order is obvious and you want maximum speed.

A good rule: **prototype top-down. Optimize bottom-up.** First,
get a correct, slow-ish solution with `@cache` — that proves the
recurrence works. Then, if perf matters, rewrite as a tabulated
loop.

## WHEN this matters

For interview problems and most production code, top-down is fine.
You'll hit bottom-up when:

- Building competitive systems (HFT, game engines) where
  microsecond perf and predictable memory matter.
- Processing huge inputs where Python's recursion limit is a
  blocker.
- Showing off in code review.

## Now: open `02_fluency.py`

Convert a top-down recursion (climb stairs) into a bottom-up loop.
