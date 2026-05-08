"""Rung 2: Fluency drill — make Tracer a context manager.

Topic: __enter__ / __exit__

`Tracer` should record events:
- on entry: append "enter" to self.events
- on exit:  append "exit"  to self.events

The body of the `with` block can call .log(message) to append a
"log:<message>" event.

Add __enter__ (returning self) and __exit__ (no exception suppression).
"""


class Tracer:
    def __init__(self) -> None:
        self.events: list[str] = []

    def log(self, msg: str) -> None:
        self.events.append(f"log:{msg}")

    # TODO: __enter__ — append "enter", return self
    # TODO: __exit__(self, exc_type, exc, tb) — append "exit", return False
