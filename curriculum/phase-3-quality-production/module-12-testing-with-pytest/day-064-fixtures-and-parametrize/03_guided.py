"""Rung 3: Guided implement — a Cache class + a fixture for it.

Topic: writing a fixture so test bodies can be one line each.

Real-world framing: a tiny in-memory cache. We'll write the unit
plus a fixture that gives every test a fresh, pre-populated cache.
"""


class Cache:
    """Tiny key->value cache."""

    def __init__(self) -> None:
        self._store: dict[str, str] = {}

    def get(self, key: str) -> str | None:
        # TODO: return self._store.get(key)
        raise NotImplementedError

    def set(self, key: str, value: str) -> None:
        # TODO: store value under key
        raise NotImplementedError

    def delete(self, key: str) -> None:
        """No-op if missing."""
        # TODO: pop with default
        raise NotImplementedError

    def size(self) -> int:
        # TODO
        raise NotImplementedError
