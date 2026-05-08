"""Rung 3: Guided implement.

Topic: @property for a computed attribute

`Rectangle` stores `width` and `height` as plain attributes. Add a
read-only property `area` that returns `width * height`, and a
read-only property `perimeter` that returns `2 * (width + height)`.

Don't add explicit setters — these should be computed on demand.
"""


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    # TODO: @property area
    # TODO: @property perimeter
