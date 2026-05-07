"""Rung 2: Fluency drill — convert inheritance to composition.

Topic: inheritance vs composition

ListWriter currently inherits from list. Refactor so it COMPOSES a
list instead. Keep the same public API: `.add(x)` appends, `.lines`
returns the underlying list.
"""


# TODO: stop inheriting from list. Instead, store a list as self.lines
# and expose .add(x) and .lines.
class ListWriter(list):
    def add(self, item: str) -> None:
        self.append(item)

    @property
    def lines(self) -> list[str]:
        return list(self)
