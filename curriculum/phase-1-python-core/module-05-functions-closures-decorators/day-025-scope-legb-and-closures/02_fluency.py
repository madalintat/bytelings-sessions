"""Rung 2: Fluency drill — scope & closures.

Topic: LEGB, nonlocal, closure capture
"""


def make_counter() -> callable:
    """Return a closure that, on each call, returns 1, 2, 3, ...

    Each independent call to make_counter() returns its own counter.
    """
    count = 0

    def step() -> int:
        # TODO: missing nonlocal; this errors on the += because of LEGB
        count += 1
        return count

    return step


def make_multiplier(factor: int) -> callable:
    """Return a function that multiplies its argument by `factor`."""
    # TODO: this returns the factor itself, not a function
    return factor


def make_listeners(n: int) -> list:
    """Return a list of n functions; the i-th returns i.

    Watch out for the late-binding trap.
    """
    # TODO: late binding; all functions return n-1
    return [lambda: i for i in range(n)]
