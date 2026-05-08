"""Rung 3: Guided — solved version.

`__init__` validates before storing so the object is always in a
consistent state — you can't create a `User("", -1)` and have it
silently lurk. `__repr__` mirrors the constructor signature so
`eval(repr(u))` would reconstruct an equivalent object (for simple
values).
"""


class User:
    def __init__(self, name: str, age: int) -> None:
        if not name:
            raise ValueError("name must not be empty")
        if age < 0:
            raise ValueError(f"age must be >= 0, got {age}")
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"User(name={self.name!r}, age={self.age})"
