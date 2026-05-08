"""Rung 3: Guided implement — solved version.

A tiny in-memory cache: get returns None for missing keys; set stores;
delete is a silent no-op on missing keys; size counts stored entries.
"""


class Cache:
    """Tiny key->value cache."""

    def __init__(self) -> None:
        self._store: dict[str, str] = {}

    def get(self, key: str) -> str | None:
        return self._store.get(key)

    def set(self, key: str, value: str) -> None:
        self._store[key] = value

    def delete(self, key: str) -> None:
        """No-op if missing."""
        self._store.pop(key, None)

    def size(self) -> int:
        return len(self._store)
