---
day: day-117-2d-dp
phase: phase-5-algorithms
module: module-24-dp-greedy-backtracking
style: build-it
---
# Day 117 — Build a 2D DP table

A 2D DP is the same recipe as yesterday, but the state has **two**
indices: a position in array A and a position in array B, or row and
column on a grid, or "first i items, capacity j."

The leap from 1D to 2D is mostly mental — you're filling a grid
instead of a row. Once you know which way to walk the grid, the rest
follows.

## Worked example: unique paths in a grid

A robot at the top-left of an m×n grid wants to reach bottom-right.
It can only move right or down. How many distinct paths?

**State:** `dp[r][c]` = number of distinct paths from (0,0) to (r,c).

**Recurrence:**
```
dp[r][c] = dp[r-1][c] + dp[r][c-1]
```

To reach (r, c), you came from above or from the left. Add up the
ways.

**Base:** `dp[0][0] = 1`. Top row and left column are all 1 (only
one way: straight along).

**Code (build it from scratch):**
```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    return dp[m-1][n-1]
```

Three lines of inner work. The fill order is "top-to-bottom,
left-to-right" — every cell's dependencies are above or to the left,
which we've already filled.

## Worked example #2: edit distance (Levenshtein)

Given two strings, the **edit distance** is the minimum number of
single-character edits (insert, delete, or replace) to transform
one into the other. The shape of every spell-checker, every diff
tool, every git merge.

**State:** `dp[i][j]` = edit distance between `a[:i]` and `b[:j]`.

**Recurrence:**
```
if a[i-1] == b[j-1]:
    dp[i][j] = dp[i-1][j-1]               # no edit needed
else:
    dp[i][j] = 1 + min(
        dp[i-1][j],     # delete from a
        dp[i][j-1],     # insert into a
        dp[i-1][j-1],   # replace
    )
```

**Base:** `dp[0][j] = j` (turn empty into b[:j] takes j inserts).
`dp[i][0] = i` (delete all of a[:i]).

**Why three options?** Each cell asks: "What was my previous state?"
You either matched a letter (diagonal, no cost), inserted (came from
the left, +1), deleted (came from above, +1), or replaced (diagonal,
+1). Min of those, then +1 if you actually edited.

The clearest 2D DP in the repertoire. Worth tracing once on paper.

## The fill-order question

For 2D DP, after writing the recurrence, ask: "Which cells does
`dp[r][c]` depend on?"

- Above and left? Fill row by row, left to right (most cases).
- Below and right? Fill bottom-up, right to left.
- Anywhere on the same row at lower column? Fill the row left to
  right, but be careful — yesterday's "iterate downward" trick for
  knapsack came from this.

This is *the* place beginners get tripped up. Always sketch the
dependency arrows on a small example before you code.

## Space optimization (when you can)

If `dp[r][c]` only depends on row r-1 and the current row, you only
need two rows of memory, not the whole table. Sometimes you can
collapse to a single rolling row. Same trick as yesterday's "two
variables instead of an array."

## WHEN you reach for 2D DP

Trigger phrases:

- "Compare/align two strings/sequences."
- "Number of paths in a grid with obstacles."
- "Pick from items with two constraints (count + budget)."
- "Match two arrays element-by-element with insert/delete cost."

Real-world hits: spell-checkers, DNA alignment (Needleman-Wunsch is
2D edit distance with a different cost matrix), `diff` and `patch`,
typing autocorrect, bioinformatics in general.

## Now: open `02_fluency.py`

A unique-paths function with a wrong fill order. Fix it.
