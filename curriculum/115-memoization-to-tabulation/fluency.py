"""Rung 2: Fluency drill — greedy vs DP recognition.

Topic: coin change — when does greedy fail?

For each of the five scenarios below, predict whether a greedy
"take the largest coin that fits" strategy produces the OPTIMAL
answer.  Write your prediction in `greedy_works(coins, target)`
using ANY heuristic you like.

The test checks your prediction against the actual greedy outcome,
then compares that to the true DP optimum.  If they agree for a
given input, greedy works; if they differ, it doesn't.

Scenarios (same order the tests use):
  1. [1, 5, 10, 25],  target 30  → greedy works
  2. [1, 4, 5],       target 8   → greedy FAILS (5+1+1+1=4 coins vs 4+4=2)
  3. [1, 3, 4],       target 6   → greedy FAILS (4+1+1=3 coins vs 3+3=2)
  4. [1, 2, 5, 10, 20, 50], target 30 → greedy works
  5. [1, 7, 10],      target 14  → greedy FAILS (10+1+1+1+1=5 vs 7+7=2)

TODO: implement `greedy_works` so it returns True/False for each
      (coins, target) pair.  Your heuristic doesn't need to be
      perfect — just get all five cases right.
"""


def greedy_works(coins: list[int], target: int) -> bool:
    """Return True if greedy gives the optimal coin count, False otherwise.

    Hint: run both strategies and compare their results.
    """
    # TODO: implement this function
    raise NotImplementedError
