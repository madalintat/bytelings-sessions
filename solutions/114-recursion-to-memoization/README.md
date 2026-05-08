---
day: 114-recursion-to-memoization
phase: phase-5-algorithms
module: module-24-dp-greedy-backtracking
style: compare
---
# Day 114 — Three lenses for the same kind of problem

You're going to spend the next week on three techniques that share one
ancestor and one weakness. The ancestor: brute-force recursion (Day 89).
The weakness: brute force takes O(2^n) or worse, and your laptop fan
will let you know.

The three lenses are **dynamic programming**, **greedy**, and
**backtracking**. Most "hard" interview problems can be solved by one
of them. The actual skill — and the thing nobody teaches well — is
*choosing which one* by recognizing what the problem looks like.

The standard textbook teaches them as three separate chapters and
hopes you figure it out. We're going to teach them as three *lenses*
you try in order, and treat picking the right one as the main lesson.

## The three lenses, in one sentence each

**DP** — *the same subproblem keeps coming back*. Cache it.
> Signal: a recursive solution where `solve(state)` is called with the
> same `state` more than once. Coin change, longest common subsequence,
> edit distance, fib.

**Greedy** — *the locally best move is also globally best, AND you can prove it*.
> Signal: a problem that decomposes into independent decisions where
> the best one at each step never has to be undone. Activity selection,
> Huffman coding, Kruskal's MST, fractional knapsack.

**Backtracking** — *try a choice, recurse, undo if it doesn't work, try the next*.
> Signal: a constraint-satisfaction shape — the answer is a *sequence of
> choices*, partial answers are checkable, and you can prune branches
> that can't possibly succeed. N-queens, sudoku, word search, generating
> all permutations under a constraint.

## How you actually pick

You read the problem. You ask three questions in this order:

1. **Can a greedy proof work?** "Always pick the largest coin first" —
   does that ALWAYS produce optimal? If yes, greedy is the cheapest.
   If no (and you'll see this on Day 115 with US coins vs the made-up
   currency `[1, 4, 5]`), greedy is wrong and you fall through.
2. **Are subproblems overlapping?** Trace the recursion in your head.
   Does `solve(state)` ever get called with the same `state` twice?
   If yes, DP. Cache it.
3. **Is the answer a sequence of choices with a prune condition?** If
   the answer SHAPE is "a set of moves where each is constrained by
   the previous," and you can detect a partial dead-end early, that's
   backtracking.

Most failures aren't because you can't implement DP. They're because
you reached for greedy when DP was needed, or DP when the state space
was actually exponential and you needed backtracking with pruning.
Wrong-lens-first is more common than wrong-implementation.

## What the next 6 days look like

| Day | Problem | First instinct | What actually works | Why |
|---|---|---|---|---|
| 115 | coin change (currency `[1, 4, 5]`, target 8) | greedy: 5+1+1+1 | DP: 4+4 | greedy fails the proof |
| 116 | 0/1 knapsack | DP: `dp[i][w] = max(take, skip)` | same | overlapping subproblems |
| 117 | N-queens | DP on board state | backtracking with pruning | state space too big to memoize |
| 118 | word break | backtracking | memoized backtracking | bridge — both lenses fit |
| 119 | activity selection | DP | greedy with exchange-argument PROOF | greedy works AND we'll show why |
| 120 | template consolidation | — | — | one-page recipe per lens |

Each day starts with the WRONG lens, demonstrates why it fails or is
overkill, and switches. The wrongness is the lesson.

## Pattern Catalog cross-refs

`bytelings patterns P-28` — memoize-recursive (the DP cache decorator).
`bytelings patterns P-27` — dfs-with-explicit-stack (backtracking's
control flow). `bytelings patterns P-29` — binary-search-on-answer
(an unrelated optimization, in the same "find the recurrence" family).

## Now: open `fluency.py`

Today's fluency is a recognition drill — five short problem
descriptions, you write down which lens you'd reach for. No code
today, just recognition muscle. Tomorrow you start writing code with
the wrong lens first.
