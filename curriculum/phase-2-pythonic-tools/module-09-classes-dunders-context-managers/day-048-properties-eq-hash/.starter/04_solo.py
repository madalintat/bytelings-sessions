"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: a class with validated property + matching eq/hash

Build a class `Temperature`:

- Stored attribute: a private `_celsius: float`.
- `__init__(self, celsius: float)`: store after validating that
  celsius >= -273.15. If not, raise ValueError.
- Property `celsius`:
    - getter returns self._celsius
    - setter accepts a float, validates again, then assigns.
- Property `fahrenheit` (read-only):
    - returns celsius * 9/5 + 32
- `__eq__` and `__hash__` compare/hash by celsius value.
- `__repr__` returns f"Temperature({self.celsius})".

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


class Temperature:
    def __init__(self, celsius: float) -> None:
        raise NotImplementedError
