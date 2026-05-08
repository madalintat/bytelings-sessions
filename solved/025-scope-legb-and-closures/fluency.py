"""Rung 2: Fluency — solved version.

Three LEGB/closure fixes:
  1. make_counter: `count += 1` inside `step` requires `nonlocal count`.
     Without it, Python treats `count` as a local variable (because of
     the assignment), but it's not defined locally yet — UnboundLocalError.
     `nonlocal count` binds the name to the enclosing scope's `count`.
  2. make_multiplier: the function returns `factor` (the int) instead of
     a function. Fix: return a lambda or nested def that takes `x` and
     returns `x * factor`.
  3. make_listeners: the classic late-binding trap. All lambdas capture
     the VARIABLE `i`, not its value at creation time. When they execute
     later, `i` is `n-1` for all of them. Fix: bind the current value
     as a default argument: `lambda i=i: i`.
"""


def make_counter() -> callable:
    """Return a closure that, on each call, returns 1, 2, 3, ..."""
    count = 0

    def step() -> int:
        nonlocal count
        count += 1
        return count

    return step


def make_multiplier(factor: int) -> callable:
    """Return a function that multiplies its argument by `factor`."""
    return lambda x: x * factor


def make_listeners(n: int) -> list:
    """Return a list of n functions; the i-th returns i."""
    return [lambda i=i: i for i in range(n)]
