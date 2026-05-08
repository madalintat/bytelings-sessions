"""Rung 4: Solo — solved version.

We catch each exception family in order of specificity. `LookupError`
covers both `KeyError` and `IndexError`. `OSError` covers
`FileNotFoundError`, `PermissionError`, and other IO errors. Any other
exception is intentionally left uncaught so it propagates to the
caller.
"""
from typing import Any, Callable


def classify_failure(callable_: Callable, *args: Any) -> tuple[str, Any]:
    try:
        return ("ok", callable_(*args))
    except LookupError:
        return ("missing", None)
    except ValueError:
        return ("bad_value", None)
    except OSError:
        return ("io", None)
