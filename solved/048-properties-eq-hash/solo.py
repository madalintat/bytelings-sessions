"""Rung 4: Solo — solved version.

`Temperature` stores one private float (`_celsius`). The `celsius`
property delegates set access through the same validation logic as
`__init__` — both paths call the setter. `fahrenheit` is read-only.
`__eq__` and `__hash__` compare by `_celsius` so `Temperature(100) ==
Temperature(100)` and they can be stored in sets.
"""
_ABS_ZERO = -273.15


class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius  # use the setter for validation

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < _ABS_ZERO:
            raise ValueError(
                f"celsius must be >= {_ABS_ZERO}, got {value}"
            )
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    def __eq__(self, other) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self._celsius == other._celsius

    def __hash__(self) -> int:
        return hash(self._celsius)

    def __repr__(self) -> str:
        return f"Temperature({self._celsius})"
