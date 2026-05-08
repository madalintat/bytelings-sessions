---
day: 120-three-templates-consolidated
phase: phase-5-algorithms
module: module-24-dp-greedy-backtracking
style: tour
---
# Day 120 — One page per lens. Print this. Tape it to your wall.

You've spent six days with the three lenses. Today is the
consolidation: one canonical template per lens, the recognition
signal, the proof obligation, and the canonical failure mode. When
a future problem walks in, you don't reach for memory of "what was
that day's solution" — you reach for these three pages.

## DP — the cache-overlapping-subproblems lens

**Recognition signal**: the recursion `solve(state)` is called with the
same `state` more than once. Or: the answer is `optimum over choices
where each choice reduces to the same problem on a smaller state`.

**Template (top-down)**:
```python
from functools import cache

@cache
def solve(state):
    if base_case(state):
        return base_value
    return aggregate(
        cost(choice) + solve(next_state(state, choice))
        for choice in choices(state)
    )
```

**Template (bottom-up)**:
```python
dp = [base for _ in range(N + 1)]      # initialize
for i in range(...):
    for j in range(...):
        dp[i][j] = aggregate(dp[i-1][j], dp[i][j-1], …)
return dp[N]
```

**Proof obligation**: none beyond the recurrence itself — DP is
correct iff the recurrence is.

**Canonical failure mode**: state space is exponential or has too
many independent dimensions. Memoization table doesn't fit, and most
cells are unreachable. Switch to backtracking with pruning.

**Examples**: fib, coin change (Day 115), 0/1 knapsack (Day 116),
LCS, edit distance, word break (Day 118).

## Greedy — the locally-optimal-is-globally-optimal lens

**Recognition signal**: the answer is built incrementally, each step
makes a *local* choice, and you can prove (via exchange argument)
that the local choice never has to be undone.

**Template**:
```python
items = sorted(items, key=greedy_key)
result = empty
for item in items:
    if compatible(item, result):
        result.append(item)
return result
```

**Proof obligation**: write the exchange argument (Day 119). If it
doesn't go through, greedy is wrong — switch to DP.

**Canonical failure mode**: a "swap" that improves locally but breaks
later validity (Day 115 coin change `[1, 4, 5]`). The disagreement
between greedy's first move and OPT's first move can't be repaired
by the swap.

**Examples**: activity selection (Day 119), Huffman, Kruskal's,
fractional knapsack (NOT 0/1), Dijkstra.

## Backtracking — the prune-the-search-tree lens

**Recognition signal**: the answer is a *sequence of choices* with a
constraint at each step. Partial answers are checkable. The state
space is too big for DP.

**Template**:
```python
def solve(state):
    if state.is_complete():
        record(state)
        return
    for choice in state.legal_next_choices():
        if not state.can_extend_with(choice):   # prune
            continue
        state.apply(choice)
        solve(state)
        state.undo(choice)                       # backtrack
```

**Proof obligation**: prove your `can_extend_with` doesn't reject any
valid completion. Pruning that's too aggressive misses solutions;
pruning that's too lax doesn't help.

**Canonical failure mode**: subproblems overlap. You're recomputing
the same subtree from many entry points. Add memoization (becomes a
DP-flavored bridge — Day 118 word break).

**Examples**: N-queens (Day 117), sudoku, permutations under
constraint, generating subsets, word search in a grid.

## The decision flowchart (one minute, every problem)

1. Can a *single greedy rule* be locally evaluated? → try the
   exchange argument. If it goes through, ship it. If not, fall
   through.
2. Does `solve(state)` get called with the *same `state` more than
   once*? → DP. Top-down with `@cache` if the recurrence is more
   readable; bottom-up if iteration is.
3. Is the answer a *tree of choices with a checkable constraint*? →
   backtracking. Add pruning. If subproblems overlap, memoize.

Most problems land cleanly in one bucket. The bridge cases (word
break, N-queens with hashed-board pruning) get *both* — that's not
a contradiction, it's the natural meeting point of the two lenses.

## Today's exercises

- **Fluency**: 8 problems, one paragraph each. Mark which lens(es).
  The diagnose helper points at the swap-breaks or the exponential
  state-space when you pick wrong.
- **Guided**: re-implement *one* problem from this module's earlier
  days using the *other* lens (e.g. coin change with backtracking
  + memoization, then notice it's just DP again).
- **Solo**: one new problem from each lens. Templates are open;
  pick one, justify the lens, ship.
- **Apply**: write a one-page cheat-sheet of YOUR lens choices, in
  YOUR words. Print it. The Solo answer key will diff against a
  reference; the Apply is yours.

## What graduating from Module 24 means

You should now look at any "find the optimum / find a sequence /
find all valid X" problem and *predict* which lens before reading
the solution. The actual code is in your fingers from M-23 onward.
The skill that's new is **lens picking**, and that's the one
interviewers are actually testing.

## Now: open `fluency.py`
