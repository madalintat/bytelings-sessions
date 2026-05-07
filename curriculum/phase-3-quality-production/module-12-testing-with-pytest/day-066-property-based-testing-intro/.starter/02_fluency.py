"""Rung 2: Fluency drill — fix the bug that hypothesis will find for you.

Topic: property-based testing.

`safe_sum(xs)` should return the sum of `xs`. The bug: it skips the
last element. Property tests in 02_fluency_test.py will fail with a
shrunk counter-example — fix it.
"""


def safe_sum(xs: list[int]) -> int:
    # TODO: bug — returns sum of all elements except the last.
    total = 0
    for i in range(len(xs) - 1):
        total += xs[i]
    return total
