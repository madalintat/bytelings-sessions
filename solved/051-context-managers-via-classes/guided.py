"""Rung 3: Guided — solved version.

`__exit__` receives the exception type as `exc_type` (None if no
exception). We check with `issubclass(exc_type, self.exc_types)` for a
type-safe check. Returning `True` suppresses the exception; returning
`False` lets it propagate.
"""


class Suppress:
    def __init__(self, *exc_types: type) -> None:
        self.exc_types = exc_types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            return False
        return issubclass(exc_type, self.exc_types)
