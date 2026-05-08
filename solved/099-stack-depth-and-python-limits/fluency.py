"""Rung 2: Fluency — solved version.

sum_iterative replaces the recursion with a for-loop. It handles
arbitrarily long lists without hitting Python's recursion limit.
"""


def sum_recursive(nums: list[int]) -> int:
    """Recursive — provided for reference. Crashes on long inputs."""
    if not nums:
        return 0
    return nums[0] + sum_recursive(nums[1:])


def sum_iterative(nums: list[int]) -> int:
    """Same answer as sum_recursive but loops instead of recurses."""
    total = 0
    for x in nums:
        total += x
    return total
