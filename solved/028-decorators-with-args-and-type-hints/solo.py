"""Rung 4: Solo — solved version.

`validate(**checks)` is a 3-layer decorator factory:
  1. `validate(**checks)` — captures the name->predicate mapping, returns decorator.
  2. `decorator(fn)` — uses `inspect.signature(fn)` to bind args at call time.
  3. `wrapped(*args, **kwargs)` — binds the call's arguments, then for each
     check name, look up the bound value and test the predicate.

Using `inspect.signature(fn).bind(*args, **kwargs).arguments` gives a dict
of parameter-name -> value regardless of whether the caller used positional
or keyword form.

Unknown check names (not in the signature) are silently ignored.
"""
import functools
import inspect
from typing import Callable


def validate(**checks: Callable) -> Callable:
    def decorator(fn: Callable) -> Callable:
        sig = inspect.signature(fn)

        @functools.wraps(fn)
        def wrapped(*args, **kwargs):
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            for name, predicate in checks.items():
                if name in bound.arguments:
                    value = bound.arguments[name]
                    if not predicate(value):
                        raise ValueError(f"invalid {name}: {value!r}")
            return fn(*args, **kwargs)

        return wrapped

    return decorator
