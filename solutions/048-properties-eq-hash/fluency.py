"""Rung 2: Fluency drill — fix the eq/hash contract.

Topic: __eq__ + __hash__

`Tag` overrides __eq__ but not __hash__, so it doesn't behave as a
dict/set key. Add __hash__ that's consistent with __eq__ (hash by name).
"""


class Tag:
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other) -> bool:
        if not isinstance(other, Tag):
            return NotImplemented
        return self.name == other.name

    # TODO: add __hash__ returning hash(self.name)
