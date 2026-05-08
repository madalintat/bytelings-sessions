"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: a small class with normalization

Build a class `Email`:

- `__init__(self, address: str)`:
   - Strip leading/trailing whitespace.
   - Lowercase the result.
   - If, after stripping, the address is empty, raise ValueError.
   - If the result does NOT contain exactly one '@', raise ValueError.
   - Store the cleaned address as self.address.

- `__repr__` returns f"Email({self.address!r})".

- A method `domain(self) -> str`: returns the part after '@'.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


class Email:
    def __init__(self, address: str) -> None:
        raise NotImplementedError
