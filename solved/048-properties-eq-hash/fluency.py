"""Rung 2: Fluency — solved version.

Python's rule: if you define `__eq__`, you must also define `__hash__`
explicitly, because Python sets `__hash__ = None` on classes that
override `__eq__` without providing `__hash__`. We hash by `name`
— the same field used in `__eq__` — so equal tags always hash the same.
"""


class Tag:
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other) -> bool:
        if not isinstance(other, Tag):
            return NotImplemented
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)
