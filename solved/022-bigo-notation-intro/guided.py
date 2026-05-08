"""Rung 3: Guided — solved version.

`has_pair_with_sum` improves the O(n^2) nested loop to O(n) using
a "complement set" approach:

  - Walk nums left to right.
  - For each x, compute `complement = target - x`.
  - If complement is already in `seen`, we've found a pair.
  - Otherwise add x to `seen` and continue.

This is O(n) total: one pass, each element checked against a set in O(1).
The `seen` set only ever contains elements we've already passed, which
ensures we use two DISTINCT indices (i != j).

Special case: a single element `[5]` with target=10 does NOT form a pair
with itself: when we check 5, `seen` is empty, so we add 5 and move on.
No j > i exists, so we return False. Correct.
"""


def has_pair_with_sum(nums: list[int], target: int) -> bool:
    """Return True iff there exist i != j with nums[i] + nums[j] == target.

    O(n) using a set of complements.

    >>> has_pair_with_sum([1, 2, 3, 4], 5)
    True
    >>> has_pair_with_sum([1, 2, 3], 100)
    False
    >>> has_pair_with_sum([3, 3], 6)
    True
    >>> has_pair_with_sum([], 0)
    False
    """
    seen: set[int] = set()
    for x in nums:
        if target - x in seen:
            return True
        seen.add(x)
    return False
