"""Rung 4: Solo — solved version.

`sum(numbers) / len(numbers)` is the textbook arithmetic mean. The
docstring's contract: empty list returns 0.0 — so guard `not numbers`
first to avoid ZeroDivisionError.

Three things to notice in the contract:
  1. Return type is float, even when the inputs are ints. The
     `/` operator gives a float in Python 3 (unlike `//`), so this
     happens automatically as long as one operand isn't itself
     special-cased.
  2. Empty list returns 0.0, not None and not raises. That's a
     design choice — see Day 60 for EAFP-vs-LBYL — but the spec is
     explicit so just follow it.
  3. The annotation `list[float]` is permissive: in practice
     callers pass list[int] | list[float] | list[Decimal]. Python's
     duck typing means the function just works on any iterable of
     things that support + and /.

For numerical hygiene on giant lists, `statistics.fmean(numbers)`
is faster and slightly more accurate (uses Kahan summation). Worth
knowing but overkill here.
"""


def mean(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)
