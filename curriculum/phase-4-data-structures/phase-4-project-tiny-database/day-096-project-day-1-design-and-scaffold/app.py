"""Tiny in-memory database — Day 1 scaffold.

Today: declare the API. Don't implement bodies. Tomorrow's day will
fill them in.
"""
from typing import Optional


class Table:
    """An in-memory table with a hash index for point lookups and a
    BST-flavored range index for range queries.

    Row schema (the dicts returned by get/range_query):
        {
            "id":         int,            # auto-assigned, unique
            "range_key":  int,            # the indexed range column
            **payload,                    # whatever was passed in
        }
    """

    def __init__(self) -> None:
        # TODO (today): initialize the hash index, the range index,
        # the next-id counter. None of the methods need to actually
        # work yet.
        self._next_id: int = 1
        self._by_id: dict = {}     # placeholder
        # The BST will live in self._by_range — leave it as None today.
        self._by_range = None

    def insert(self, range_key: int, payload: dict) -> int:
        """Add a row; return its newly assigned id."""
        # TODO (Day 2): implement
        raise NotImplementedError

    def get(self, row_id: int) -> Optional[dict]:
        """Return the row, or None if no such id."""
        # TODO (Day 2): implement
        raise NotImplementedError

    def delete(self, row_id: int) -> bool:
        """Remove the row. Return True if removed, False if no such id."""
        # TODO (Day 2): implement
        raise NotImplementedError

    def range_query(self, lo: int, hi: int) -> list[dict]:
        """Return every row whose range_key is in [lo, hi], sorted ascending."""
        # TODO (Day 2): implement
        raise NotImplementedError

    def __len__(self) -> int:
        # We can implement THIS one today: it's trivially len(self._by_id).
        return len(self._by_id)
