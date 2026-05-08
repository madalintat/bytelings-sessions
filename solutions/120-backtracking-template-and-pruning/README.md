---
day: day-120-backtracking-template-and-pruning
phase: phase-5-algorithms
module: module-24-dp-greedy-backtracking
style: metaphor
---
# Day 120 — Walking through a hedge maze with breadcrumbs

You're in a hedge maze with branching paths. You explore by:

1. Walking down a path until you hit a dead end or the goal.
2. If it's a dead end, you walk back to the last junction with
   un-explored options.
3. You take a different option from there.
4. Repeat until you've found the goal — or you've explored every
   branch and given up.

You drop breadcrumbs on the floor as you walk in, and pick them up
on the way out. After you leave a path, the breadcrumbs are gone —
no trace you were ever there. Future you, on a different path, can
walk through it freshly.

That's backtracking. DFS with **explicit undo**.

## The template (memorize this)

Every backtracking problem follows the same shape:

```python
def backtrack(state, partial):
    if is_solution(partial):
        record(partial)
        return
    for choice in choices(state):
        if not is_valid(state, choice):
            continue                     # PRUNE
        apply(state, choice, partial)    # take the choice
        backtrack(state, partial)
        undo(state, choice, partial)     # UNDO — pick up the breadcrumb
```

Five lines plus pruning. Once you internalize this, every
backtracking problem is "fill in the four blanks."

## Worked example: generate all permutations

```python
def permutations(arr):
    out = []
    used = [False] * len(arr)
    partial = []

    def backtrack():
        if len(partial) == len(arr):
            out.append(partial[:])      # copy! partial keeps changing
            return
        for i, x in enumerate(arr):
            if used[i]:
                continue
            partial.append(x); used[i] = True
            backtrack()
            partial.pop();    used[i] = False  # UNDO

    backtrack()
    return out
```

Five-line template, filled in. The `used` array is the breadcrumb
trail — it gets set on entry and unset on exit. By the time the
function returns from the top level, every cell of `used` is False
again, exactly as it started.

## Pruning is where backtracking earns its keep

Without pruning, backtracking is just brute force in a fancy hat.
The whole point is to **prune branches that can't lead to a solution
before you walk down them**.

In permutations, the pruning is "skip elements I've already used."
In Sudoku, it's "skip a digit that already appears in this row,
column, or 3×3 box." In N-queens, it's "skip a column that's already
got a queen, or a diagonal that's threatened."

The better your pruning, the smaller your search tree, the faster
your solver. With good pruning, an N-queens solver handles N=20 in
seconds; without pruning, it explodes at N=8.

## When to reach for backtracking

Backtracking is the right tool for **constraint-satisfaction** and
**enumeration** problems where you're looking for a *configuration*,
not a number:

- Sudoku, crossword, KenKen, and other puzzle solvers.
- N-queens, knight's tour, Latin squares.
- Generating all permutations / combinations / subsets.
- Word break (with full path), partition strings into palindromes.
- Finding a path through a maze (PP5 will use this).
- Constraint solving in scheduling: "assign these tasks to these
  rooms, no conflicts."

## Backtracking vs DP: the difference

DP: "what's the optimal answer?" Solve once, memoize.

Backtracking: "what are all the configurations?" Walk every valid
path; emit each one.

Some problems blur the line — "find one configuration" can use
either. As a rule: if the answer is a *number* (count, max, min),
think DP. If the answer is a *list of things* (paths, arrangements),
think backtracking.

## A common mistake

Forgetting the undo step. Without it, breadcrumbs accumulate and
parallel branches contaminate each other — your solver finds one
solution then gets stuck because the trail is messed up. **Every
`apply` needs a matching `undo`.**

If undo is awkward, an alternative is to pass an immutable copy
("here's the partial with this choice added") instead of mutating.
Slower but bug-free.

## Now: open `fluency.py`

A subset generator that forgot to undo. Find the missing line.
