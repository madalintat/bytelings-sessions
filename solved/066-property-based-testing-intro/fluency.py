"""Rung 2: Fluency drill — solved version.

Bug: range(len(xs) - 1) skips the last element. Fix: range(len(xs)).
The property test (sum invariant) immediately finds a counter-example
like [1] where the result should be 1 but was 0.
"""


def safe_sum(xs: list[int]) -> int:
    total = 0
    for i in range(len(xs)):
        total += xs[i]
    return total
