---
day: 117-n-queens-backtracking
phase: phase-5-algorithms
module: module-24-dp-greedy-backtracking
style: build-it
---
# Day 117 — N-queens: when the state space is too big for DP

Day 116 was DP at home. Today's problem looks like DP from one angle
and is actually backtracking. The recognition signal is the *size of
the state space*, and you're going to feel it.

## The problem

```
Place N queens on an N×N chessboard so that no two queens attack each
other (same row, same column, same diagonal). Return all valid
configurations as lists of column-per-row.
```

N=4: 2 solutions. N=8: 92. N=12: 14,200. The numbers grow fast, but
the *valid* placements are a tiny fraction of all 4^N possible ones.

## Why DP fails here

A DP solution would need a state. Natural one: "rows processed so far
+ which queens are where." But the queen positions are *part* of the
state — you can't compress them. The state space is at least `N!`,
which for N=12 is half a billion entries. Memoizing that table is
hopeless and most cells never get visited anyway.

Whenever the state space is exponential AND most of it is dead
(invalid), DP is the wrong lens. You don't want a *table*; you want a
*search that prunes invalid branches early*. That's backtracking.

## The backtracking shape (memorize this)

```
def solve(state):
    if state.is_complete():
        record(state)
        return
    for choice in state.legal_next_choices():
        state.apply(choice)
        solve(state)
        state.undo(choice)        # ← the backtrack
```

Four blanks to fill every time:
1. **State** — a partial solution. For N-queens: a list of column
   indices, one per row processed.
2. **is_complete** — when do we record? When `len(cols) == N`.
3. **legal_next_choices** — at row `r`, which columns are safe? Any
   column not equal to a previous queen's column AND not on a
   diagonal (`abs(r - r') == abs(c - c')`).
4. **undo** — pop the last column.

```python
def n_queens(n: int) -> list[list[int]]:
    solutions: list[list[int]] = []
    cols: list[int] = []

    def is_safe(row: int, col: int) -> bool:
        for r, c in enumerate(cols):
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True

    def solve(row: int) -> None:
        if row == n:
            solutions.append(cols.copy())
            return
        for col in range(n):
            if is_safe(row, col):
                cols.append(col)
                solve(row + 1)
                cols.pop()                 # backtrack

    solve(0)
    return solutions
```

## The two backtracking superpowers

1. **Prune early.** `is_safe` runs *before* recursing. A collision at
   row 1 prevents the entire `solve(2..n)` subtree. For N=8 this
   skips roughly 99.9% of the brute-force tree.
2. **The undo is what makes it backtracking, not DFS.** You explore
   one branch fully, *back out*, try the next. `cols.pop()` is the
   distinguishing line.

## Today's exercises

- **Fluency**: trace `solve(0)` for N=4 by hand. The diagnose helper
  catches the off-by-one in the diagonal check (a common bug — using
  `r - r' == c - c'` instead of `abs(...)`, missing the
  anti-diagonal).
- **Guided**: implement `is_safe` only. The recursion is provided.
- **Solo**: full N-queens, returning all solutions in pretty-board
  format (`. . . Q / Q . . . / …`).
- **Apply**: extend to count-only (don't enumerate, just count). For
  N=14 the count is ~365,596. Your code prints that in under a
  second if pruning is right; hours if it isn't.

## Pattern Catalog

`bytelings patterns P-27` — dfs-with-explicit-stack. Today's
recursion is implicit DFS; tomorrow's word-break shows the explicit
stack form. Both have the *try → recurse → undo* shape.

## Recognition signal recap

DP wanted a *table* indexed by compact state. Backtracking wants a
*search tree* that you prune. When the state has many independent
dimensions or grows combinatorially, you're in backtracking land.
Don't draw the DP table — draw the search tree, mark dead branches.

## Now: open `fluency.py`
