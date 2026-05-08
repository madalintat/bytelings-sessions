"""Rung 3: Guided implement.

Topic: __init__ with validation + __repr__

Implement a class `User`:
- `__init__(self, name: str, age: int)` — store both as attributes.
- If `age < 0`, raise ValueError.
- If `name` is empty, raise ValueError.
- `__repr__` returns f"User(name={name!r}, age={age})".

Don't use @dataclass — write the dunders by hand.
"""


class User:
    def __init__(self, name: str, age: int) -> None:
        # TODO: validate name (non-empty) and age (>= 0). Then store both.
        raise NotImplementedError

    # TODO: __repr__
