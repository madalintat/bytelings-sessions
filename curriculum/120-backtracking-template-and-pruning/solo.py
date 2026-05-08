"""Rung 4: Solo.

Topic: largest rectangle in histogram.

Given a list of bar heights, find the area of the largest rectangle
that can be formed within the bars.

>>> largest_rectangle_in_histogram([2, 1, 5, 6, 2, 3])
10

>>> largest_rectangle_in_histogram([2, 4])
4

Lens choice: this problem is best solved with a monotonic stack
(related to P-27 dfs-with-explicit-stack). A DP approach works but
uses O(n^2) space for left/right boundary arrays. The stack approach
is O(n) time and O(n) space.

Algorithm (monotonic stack):
- Maintain a stack of indices of bars in non-decreasing height order.
- For each bar i: while the stack is non-empty and heights[stack[-1]] >= heights[i],
    pop index k; the width of the rectangle with height heights[k] extends
    from (stack[-1] + 1) to (i - 1).
- After the loop, drain the stack similarly (treating the right boundary
  as len(heights)).
- Track the maximum area seen.

Tests in solo_test.py are HIDDEN.

Patterns: P-27 (dfs-with-explicit-stack).
"""


def largest_rectangle_in_histogram(heights: list[int]) -> int:
    raise NotImplementedError
