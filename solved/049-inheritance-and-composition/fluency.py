"""Rung 2: Fluency — solved version.

`ListWriter` previously inherited from `list`, exposing every list
method as part of its API — far more than needed. Composition hides
the list behind `self.lines` and exposes only `.add()`. This is the
"has-a" vs "is-a" distinction: a ListWriter *has* a list, it is not
a list.
"""


class ListWriter:
    def __init__(self) -> None:
        self.lines: list[str] = []

    def add(self, item: str) -> None:
        self.lines.append(item)
