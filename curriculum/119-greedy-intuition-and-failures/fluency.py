"""Rung 2: Fluency drill — greedy or not?

Topic: exchange argument as the proof technique.

Five problem descriptions below. For each, return "greedy" if the
greedy approach provably works (an exchange argument goes through),
or "needs DP" if greedy fails (coin change [1,4,5] counterexample
or similar).

Problems:
  1 — activity selection (maximise non-overlapping intervals, sort by finish)
  2 — coin change with denominations [1, 4, 5]  (find minimum coins for 8)
  3 — Huffman coding (build optimal prefix-free code from frequencies)
  4 — 0/1 knapsack (items cannot be split)
  5 — fractional knapsack (items CAN be split by weight)

Two of the five need DP; three are correct with greedy.

TODO: implement `classify` so the tests pass.
"""


def classify(problem_id: int) -> str:
    """Return "greedy" or "needs DP" for each of the five problems.

    The exchange argument must hold for "greedy"; otherwise "needs DP".
    """
    raise NotImplementedError
