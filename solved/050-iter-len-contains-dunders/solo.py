"""Rung 4: Solo — solved version.

`OrderedSet` uses a `dict` as the primary store (dicts preserve
insertion order since Python 3.7) and a `set` shadow for O(1)
membership tests. `add` inserts into both; `__contains__` queries the
set; `__iter__` walks the dict's keys; `__len__` queries the dict.

Using a dict as the primary container (with dummy `True` values) would
also work — dicts give O(1) `__contains__` too — but the explicit set
makes the O(1) contract obvious.
"""


class OrderedSet:
    def __init__(self, items=None) -> None:
        self._dict: dict = {}
        self._set: set = set()
        if items is not None:
            for item in items:
                self.add(item)

    def add(self, item) -> None:
        if item not in self._set:
            self._dict[item] = None
            self._set.add(item)

    def __len__(self) -> int:
        return len(self._dict)

    def __iter__(self):
        return iter(self._dict)

    def __contains__(self, item) -> bool:
        return item in self._set

    def __repr__(self) -> str:
        return f"OrderedSet({list(self)!r})"
