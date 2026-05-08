"""Rung 2: Fluency drill — give Counter a real __repr__.

Topic: __init__ + __repr__

`Counter` works, but `repr(c)` shows the unhelpful default
`<...Counter object at 0x...>`. Add a `__repr__` that returns
`Counter(name='cards', value=3)`.
"""


class Counter:
    def __init__(self, name: str, start: int = 0) -> None:
        self.name = name
        self.value = start

    def increment(self) -> None:
        self.value += 1

    # TODO: add __repr__ returning f"Counter(name={self.name!r}, value={self.value})"
