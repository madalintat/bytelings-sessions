"""Rung 4: Solo — solved version.

Monotonic stack solution (P-27 dfs-with-explicit-stack).

The stack stores bar indices in non-decreasing height order. When a
shorter bar is encountered, bars popped from the stack form the
right boundary of their rectangle; the new stack-top (after popping)
forms the left boundary.

A sentinel 0-height bar appended to heights ensures all bars are
flushed from the stack at the end.

Time: O(n) — each index is pushed and popped at most once.
Space: O(n) for the stack.
"""


def largest_rectangle_in_histogram(heights: list[int]) -> int:
    """Return the area of the largest rectangle in the histogram."""
    if not heights:
        return 0

    stack: list[int] = []   # indices of bars in non-decreasing height order
    max_area = 0

    # Append a sentinel to flush all remaining bars at the end.
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            # Width extends to the current bar (exclusive) from after
            # the new stack-top (inclusive), or from 0 if the stack is empty.
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area
