"""Rung 3: Guided — implement `power` with the call you'd actually make.

Topic: tracing the recursion to see how values bubble up

Compute a ** b for non-negative integer b, recursively. Trace what
happens for power(2, 5):

    power(2, 5) = 2 * power(2, 4)
                = 2 * (2 * power(2, 3))
                = 2 * (2 * (2 * power(2, 2)))
                = ...
                = 2 * 2 * 2 * 2 * 2 * 1
                = 32

Base case: anything to the 0 is 1.

>>> power(2, 0)
1
>>> power(3, 4)
81
>>> power(7, 1)
7

(No `**` and no `math.pow`. The recursive call IS the point.)
"""


def power(a: int, b: int) -> int:
    raise NotImplementedError
