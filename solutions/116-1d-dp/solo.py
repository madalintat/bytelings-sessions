"""Rung 4: Solo.

Topic: 0/1 Knapsack — but specifically the easier "can we fill this
exactly?" subset-sum variant.

Given a list of positive ints `weights` and a target `total`, return
True iff some subset sums to exactly `total`.

>>> subset_sum([3, 34, 4, 12, 5, 2], 9)
True   # 4 + 5 = 9, or 7+2 etc.
>>> subset_sum([1, 2, 3], 7)
False
>>> subset_sum([], 0)
True   # empty subset sums to 0
>>> subset_sum([1, 2, 3], 0)
True   # always possible

Hints:
- 1D bottom-up: dp[t] = True iff some subset sums to t.
- Initialize dp = [True] + [False] * total.
- For each w in weights, update dp from t = total down to t = w:
    if dp[t - w]: dp[t] = True
  (Iterate downward so each weight is used at most once — this is
  the 0/1 trick.)
- Return dp[total].

Tests in 04_solo_test.py are HIDDEN.

Patterns: P-04 (dispatch-by-dict), P-11 (reduce-with-identity).
"""


def subset_sum(weights: list[int], total: int) -> bool:
    raise NotImplementedError
