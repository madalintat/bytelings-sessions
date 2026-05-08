"""Rung 3: Guided — solved version.

`@property` turns a method into a computed attribute. No setter is
defined, so assigning to `rect.area` raises `AttributeError`. Both
properties are computed from the raw `width` and `height` every time
they are accessed — no caching needed for cheap arithmetic.
"""


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    @property
    def area(self) -> int:
        return self.width * self.height

    @property
    def perimeter(self) -> int:
        return 2 * (self.width + self.height)
