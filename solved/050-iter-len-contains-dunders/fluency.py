"""Rung 2: Fluency — solved version.

Each dunder is a one-liner that delegates to the underlying list.
Implementing all three unlocks the full Python container protocol:
`len(bag)`, `x in bag`, and `for x in bag` all work, as does anything
in the standard library that depends on these (e.g. `sorted`, `list`,
`tuple`).
"""


class Bag:
    def __init__(self, items: list = None) -> None:
        self._items = list(items) if items else []

    def add(self, item) -> None:
        self._items.append(item)

    def __len__(self) -> int:
        return len(self._items)

    def __contains__(self, item) -> bool:
        return item in self._items

    def __iter__(self):
        return iter(self._items)
