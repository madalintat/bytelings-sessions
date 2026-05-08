"""Rung 2: Fluency drill — solved version.

The bug: `total / i` raises ZeroDivisionError on the first iteration
because `enumerate` starts at 0. Fix: use `i + 1` as the divisor, or
pass `start=1` to enumerate. The breakpoint is removed before shipping.
"""


def running_average(values: list[float]) -> list[float]:
    total = 0.0
    averages: list[float] = []
    for i, v in enumerate(values):
        total += v
        averages.append(total / (i + 1))
    return averages
