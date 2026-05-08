"""Day 101 — Project Day 2: full Table implementation.

The Table maintains two indices in sync:
  _by_id:    dict[int, dict]          — O(1) point lookup
  _by_range: sorted list of (range_key, id) tuples — O(log n) range scan
             (Using a sorted list + bisect is simpler than a full BST
             for this project; the algorithmic lesson is the same.)

Row dict shape returned to callers:
    {"id": <int>, "range_key": <int>, **payload}
"""
import bisect
from typing import Optional


class Table:
    """Tiny in-memory database table with hash + range indices."""

    def __init__(self) -> None:
        self._by_id: dict[int, dict] = {}
        self._by_range: list[tuple] = []   # sorted (range_key, id) tuples
        self._next_id: int = 1

    def insert(self, range_key: int, payload: dict) -> int:
        """Add a new row. Returns the assigned id."""
        row_id = self._next_id
        self._next_id += 1
        row = {"id": row_id, "range_key": range_key, **payload}
        self._by_id[row_id] = row
        bisect.insort(self._by_range, (range_key, row_id))
        return row_id

    def get(self, row_id: int) -> Optional[dict]:
        """Return the row dict, or None if no such id."""
        return self._by_id.get(row_id)

    def delete(self, row_id: int) -> bool:
        """Remove the row. True if removed, False if missing."""
        row = self._by_id.pop(row_id, None)
        if row is None:
            return False
        key = (row["range_key"], row_id)
        idx = bisect.bisect_left(self._by_range, key)
        if idx < len(self._by_range) and self._by_range[idx] == key:
            del self._by_range[idx]
        return True

    def range_query(self, lo: int, hi: int) -> list[dict]:
        """All rows where lo <= range_key <= hi, sorted ascending by range_key."""
        lo_idx = bisect.bisect_left(self._by_range, (lo, -1))
        hi_idx = bisect.bisect_right(self._by_range, (hi, float("inf")))
        result = []
        for rk, rid in self._by_range[lo_idx:hi_idx]:
            row = self._by_id.get(rid)
            if row is not None:
                result.append(row)
        return result

    def __len__(self) -> int:
        return len(self._by_id)
