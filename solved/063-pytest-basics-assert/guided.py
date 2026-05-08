"""Rung 3: Guided implement — solved version.

A per-key request counter backed by a plain dict. The hit() method
returns the new value after incrementing; value() returns 0 for unseen
keys; reset() clears a key (or silently no-ops if absent).
"""


class Counter:
    """Per-key request counter."""

    def __init__(self) -> None:
        self._counts: dict[str, int] = {}

    def hit(self, key: str) -> int:
        """Increment count for `key` and return the new value."""
        self._counts[key] = self._counts.get(key, 0) + 1
        return self._counts[key]

    def value(self, key: str) -> int:
        """Return current count for `key`, or 0 if unseen."""
        return self._counts.get(key, 0)

    def reset(self, key: str) -> None:
        """Reset count for `key` to 0. No-op if unseen."""
        self._counts.pop(key, None)
