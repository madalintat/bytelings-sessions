"""Rung 4: Solo implement.

Topic: a `validate(**checks)` decorator

Implement `validate(**checks)`:

- `checks` is keyword args mapping a parameter name -> a predicate
  function (a single-arg function returning bool).
- The wrapped function gets each named argument's value validated:
  if predicate(value) is falsy, raise ValueError(f"invalid {name}: {value!r}").
- The check applies whether the arg was passed positionally or by keyword.
- Use inspect.signature so positional args bind to their proper name.
- Unknown check names (not actual parameters of fn) are silently ignored.
- functools.wraps preserves fn's __name__.

Examples:
    @validate(x=lambda x: x > 0, y=lambda y: y < 100)
    def f(x, y):
        return x + y

    f(1, 2)        # 3
    f(0, 1)        # ValueError: invalid x: 0
    f(1, 100)      # ValueError: invalid y: 100
    f(1, y=2)      # 3 (kwargs work)

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""
import functools
import inspect
from typing import Callable


def validate(**checks: Callable) -> Callable:
    raise NotImplementedError
