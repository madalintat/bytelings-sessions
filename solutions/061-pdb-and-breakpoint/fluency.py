"""Rung 2: Fluency drill — find the bug with breakpoint().

Topic: using pdb / breakpoint to investigate a running program.

`running_average` should return [v0, (v0+v1)/2, (v0+v1+v2)/3, ...].
It crashes on a ZeroDivisionError. Drop a `breakpoint()` line, run
the test, inspect `i` and `total`. Fix the off-by-one.

When the test is green, REMOVE the `breakpoint()` line.
"""


def running_average(values: list[float]) -> list[float]:
    total = 0.0
    averages: list[float] = []
    for i, v in enumerate(values):
        # TODO (debug): drop a breakpoint() here, inspect i and total,
        # then fix the divisor below.
        total += v
        averages.append(total / i)  # TODO: this divisor is wrong on i=0
    return averages
