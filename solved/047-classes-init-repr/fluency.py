"""Rung 2: Fluency — solved version.

Without `__repr__`, `repr(c)` falls back to the default
`<__main__.Counter object at 0xADDRESS>`. Adding `__repr__` that
returns an eval-able string makes the object self-describing in the
REPL and in test failure messages.
"""


class Counter:
    def __init__(self, name: str, start: int = 0) -> None:
        self.name = name
        self.value = start

    def increment(self) -> None:
        self.value += 1

    def __repr__(self) -> str:
        return f"Counter(name={self.name!r}, value={self.value})"
