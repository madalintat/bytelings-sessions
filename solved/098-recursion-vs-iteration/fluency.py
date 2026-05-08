"""Rung 2: Fluency — solved version.

max_in_list: the recursive version hits RecursionError on long inputs
  because Python's default recursion limit is ~1000. The fix is a
  simple for-loop accumulator, which uses O(1) stack space regardless
  of input length.

flatten: the iterative version only peels one level (it extends with
  the list items but doesn't recurse into them). The recursive version
  handles arbitrary depth by recursing into any sub-list it finds.
"""


def max_in_list(nums: list[int]) -> int:
    """Return the largest int in a non-empty list. Iterative."""
    best = nums[0]
    for x in nums[1:]:
        if x > best:
            best = x
    return best


def flatten(items: list) -> list:
    """Return a flat list of all ints inside, no matter how deeply nested."""
    result = []
    for x in items:
        if isinstance(x, list):
            result.extend(flatten(x))
        else:
            result.append(x)
    return result
