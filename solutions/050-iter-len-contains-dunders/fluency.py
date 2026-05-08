"""Rung 2: Fluency drill — make Bag a real container.

Topic: __len__, __contains__, __iter__

Add the three dunders so:
    len(bag)        works
    x in bag        works
    for x in bag:   works
"""


class Bag:
    def __init__(self, items: list = None) -> None:
        self._items = list(items) if items else []

    def add(self, item) -> None:
        self._items.append(item)

    # TODO: __len__ returning len(self._items)
    # TODO: __contains__(self, item) returning whether item is in self._items
    # TODO: __iter__ returning iter(self._items)
