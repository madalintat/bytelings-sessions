"""Rung 2: Fluency drill — pick the right tool.

Topic: recursion vs iteration

`max_in_list` is currently recursive but the data is flat — this
will hit RecursionError on long lists. Rewrite as a loop.

`flatten` is currently iterative but only goes one level deep — it
needs to handle arbitrarily nested lists. Rewrite as recursion.
"""


def max_in_list(nums: list[int]) -> int:
    """Return the largest int in a non-empty list."""
    # TODO: rewrite this iteratively (a single for-loop)
    if len(nums) == 1:
        return nums[0]
    sub = max_in_list(nums[1:])
    return nums[0] if nums[0] > sub else sub


def flatten(items: list) -> list:
    """Return a flat list of all ints inside, no matter how deeply nested."""
    # TODO: rewrite recursively so it handles arbitrary depth
    result = []
    for x in items:
        if isinstance(x, list):
            result.extend(x)   # only handles ONE level — broken for deep nesting
        else:
            result.append(x)
    return result
