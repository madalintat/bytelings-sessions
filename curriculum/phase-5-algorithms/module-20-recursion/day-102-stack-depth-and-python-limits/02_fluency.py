"""Rung 2: Fluency drill — convert recursion to an explicit stack.

Topic: Python's recursion limit, and the iterative-stack workaround.

`sum_recursive` works on small lists but RecursionErrors on long ones
because Python's default recursion limit is 1000. Rewrite
`sum_iterative` so it returns the same answer using a single while
loop and no recursion (you don't actually need a stack for this one
since it's flat — just a loop).
"""


def sum_recursive(nums: list[int]) -> int:
    """Recursive — provided for reference. Crashes on long inputs."""
    if not nums:
        return 0
    return nums[0] + sum_recursive(nums[1:])


def sum_iterative(nums: list[int]) -> int:
    """Same answer as sum_recursive but loops instead of recurses."""
    # TODO: write the loop version
    raise NotImplementedError
