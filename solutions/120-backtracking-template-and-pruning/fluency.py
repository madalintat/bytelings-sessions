"""Rung 2: Fluency drill — which lens?

Topic: one canonical template per lens (DP / greedy / backtracking),
recognition signal, proof obligation, failure mode.

Eight short problem descriptions. For each, return the set of lenses
that apply. Two problems are bridge cases that need 2 lenses.

Valid lens names: "dp", "greedy", "backtracking"

Problems:
  1 — activity selection (maximise non-overlapping intervals)
  2 — coin change, minimise coins (arbitrary denominations)
  3 — generate all permutations of a list
  4 — shortest path in a weighted graph (non-negative weights)
  5 — word break with memoization (can string be segmented into words)
  6 — 0/1 knapsack
  7 — generate all valid parenthesizations of n pairs
  8 — longest common subsequence of two strings

Two of these require more than one lens.

TODO: implement `pick_lens` so the tests pass.
"""


def pick_lens(problem_id: int) -> set[str]:
    """Return the set of applicable lenses for each problem.

    Most problems land in exactly one bucket. Bridge cases return 2.
    """
    raise NotImplementedError
