"""Rung 3: Guided implement.

Topic: improve a quadratic algorithm to linear with a set

Implement `has_pair_with_sum(nums, target)`: True iff any two distinct
INDICES i, j have nums[i] + nums[j] == target. Make it O(n), not O(n^2).
"""


def has_pair_with_sum(nums: list[int], target: int) -> bool:
    """Return True iff there exist i != j with nums[i] + nums[j] == target.

    Must run in O(n). Use a set of "complements seen so far."

    >>> has_pair_with_sum([1, 2, 3, 4], 5)
    True
    >>> has_pair_with_sum([1, 2, 3], 100)
    False
    >>> has_pair_with_sum([3, 3], 6)
    True
    >>> has_pair_with_sum([], 0)
    False
    >>> has_pair_with_sum([5], 5)
    False
    """
    # TODO: walk nums; for each x check if (target - x) was already seen.
    raise NotImplementedError
