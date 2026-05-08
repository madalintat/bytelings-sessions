"""Rung 2: Fluency — solved version.

`__enter__` runs on entry to `with`, records the event, and returns
`self` so the `as` clause gives access to the Tracer instance.
`__exit__` runs on exit; returning `False` (or `None`) means exceptions
are not suppressed — they propagate to the caller.
"""


class Tracer:
    def __init__(self) -> None:
        self.events: list[str] = []

    def log(self, msg: str) -> None:
        self.events.append(f"log:{msg}")

    def __enter__(self):
        self.events.append("enter")
        return self

    def __exit__(self, exc_type, exc, tb):
        self.events.append("exit")
        return False
