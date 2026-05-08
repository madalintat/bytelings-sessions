"""Day 100 — Project Day 1: Table skeleton.

The Table exposes a clean five-method interface backed by two indices:
  - self._by_id: dict[int, dict]       O(1) point lookup
  - self._by_range: a BST keyed by (range_key, id) tuples

Today's deliverable is the stub only. Methods raise NotImplementedError
so the interface tests can be written and watched fail.
"""
from typing import Optional


class Table:
    """Tiny in-memory database table with hash + range indices."""

    def __init__(self) -> None:
        self._by_id: dict[int, dict] = {}
        self._next_id: int = 1

    def insert(self, range_key: int, payload: dict) -> int:
        """Add a new row. Returns the assigned id."""
        raise NotImplementedError

    def get(self, row_id: int) -> Optional[dict]:
        """Return the row dict, or None if no such id."""
        raise NotImplementedError

    def delete(self, row_id: int) -> bool:
        """Remove the row. True if removed, False if missing."""
        raise NotImplementedError

    def range_query(self, lo: int, hi: int) -> list[dict]:
        """All rows where lo <= range_key <= hi, sorted ascending."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
