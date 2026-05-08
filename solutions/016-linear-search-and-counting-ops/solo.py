"""Rung 4: Solo implement.

Topic: find the FIRST pair (i, j) i<j with a target sum

Implement `find_pair_with_sum(nums, target)`:

- Return the first (i, j) with i < j such that nums[i] + nums[j] == target.
- Return None if no such pair exists.
- "First" means: smallest i; for the same i, smallest j.

Examples:
    find_pair_with_sum([1, 2, 3, 4], 5)   -> (0, 3)   # 1+4
    find_pair_with_sum([1, 2, 3, 4], 100) -> None
    find_pair_with_sum([], 0)             -> None
    find_pair_with_sum([3, 3], 6)         -> (0, 1)

Naive O(n^2) is fine for this rung. We'll improve it with sets later.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


def find_pair_with_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    raise NotImplementedError
