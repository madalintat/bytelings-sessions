"""Rung 4: Solo — solved version.

`MemoryStore` wraps a plain dict. `Logger` composes a store (any
object with `.save`/`.load`) rather than inheriting from it — this
allows the test to inject a fake double without subclassing. The
`count` property returns `self._n`, which is incremented on each
`info` call.
"""


class MemoryStore:
    def __init__(self) -> None:
        self._data: dict = {}

    def save(self, key: str, value) -> None:
        self._data[key] = value

    def load(self, key: str):
        return self._data[key]


class Logger:
    def __init__(self, store) -> None:
        self._store = store
        self._n = 0

    def info(self, msg: str) -> None:
        self._store.save(f"info-{self._n}", msg)
        self._n += 1

    @property
    def count(self) -> int:
        return self._n
