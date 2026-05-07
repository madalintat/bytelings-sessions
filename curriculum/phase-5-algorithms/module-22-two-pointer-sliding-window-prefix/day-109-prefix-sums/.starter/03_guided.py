"""Rung 3: Guided — count subarrays with sum equal to k.

Topic: prefix sums + a hash map of "sums I've seen".

Given a list of ints (positive, negative, or zero) and an int k,
return the COUNT of contiguous subarrays whose sum equals exactly k.

>>> count_subarrays_with_sum([1, 1, 1], 2)
2     # [1,1] starting at 0; [1,1] starting at 1
>>> count_subarrays_with_sum([1, 2, 3], 3)
2     # [1,2] and [3]
>>> count_subarrays_with_sum([1, -1, 1, -1], 0)
4     # multiple zero-sum subarrays

The classic algorithm:
- prefix sum running total `s`.
- Hash map `seen` of (prefix_sum -> how many times we've seen it).
  Start with seen[0] = 1 (the empty prefix).
- For each x in arr:
    s += x
    answer += seen.get(s - k, 0)
    seen[s] = seen.get(s, 0) + 1
- Return answer. O(n).

Hint on why: a subarray summing to k means two prefix sums differ by
k. So at each step, count prior prefix sums equal to s - k.
"""


def count_subarrays_with_sum(arr: list[int], k: int) -> int:
    raise NotImplementedError
