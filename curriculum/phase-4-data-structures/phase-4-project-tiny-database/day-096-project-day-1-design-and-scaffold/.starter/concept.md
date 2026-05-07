---
day: day-096-project-day-1-design-and-scaffold
phase: phase-4-data-structures
module: phase-4-project-tiny-database
style: story
---
# Day 96 — Project Day 1: design and scaffold

You're building a tiny in-memory database. Today is design day.
Don't write the implementation yet — write the *interface*, write
the tests for the interface, watch them fail, and stop. Tomorrow
you'll fill in the bodies.

## The brief, restated

A `Table` holds rows. Each row has at minimum:
- an `id` (auto-assigned, unique, integer)
- a `range_key` (an integer — say, `age`, `score`, `timestamp`)
- a `payload` (anything else; we'll just use a `dict`)

The table maintains two indices, kept in sync:
- **hash index**: `id -> row` for O(1) point lookup
- **BST-flavored range index**: ordered by `range_key`, supporting
  inclusive range scans

## Today's API design

```python
class Table:
    def insert(self, range_key: int, payload: dict) -> int:
        """Add a new row. Returns the assigned id."""

    def get(self, row_id: int) -> Optional[dict]:
        """Return the row dict, or None if no such id."""

    def delete(self, row_id: int) -> bool:
        """Remove the row. True if removed, False if no such id."""

    def range_query(self, lo: int, hi: int) -> list[dict]:
        """All rows where lo <= range_key <= hi, sorted ascending by range_key."""

    def __len__(self) -> int: ...
```

Each row dict the user gets back should include the `id` and the
`range_key` (so callers can identify it), plus the payload fields.

## Today's deliverable

- `app.py` with the `Table` class skeleton — methods declared,
  raising `NotImplementedError`.
- `app_test.py` with the interface tests:
  - empty table has length 0
  - insert returns a fresh integer
  - get on a missing id returns None
  - delete on a missing id returns False
  - range_query on empty table returns []
  - the *minimum* invariant: insert, then get, returns the row

You'll watch the tests fail today. (Some will pass — like the empty-
table ones — if your skeleton starts with `len = 0`.)

## A design question to think through

You have two columns: an equality column (id) and a range column.
But what if two rows share the same range_key (two people aged 30)?
The BST is a *set*, not a multimap. You have three options:
- store **a set of row IDs** at each BST value
- store **(range_key, id) tuples** in the BST so they're all unique
- forbid duplicates at the API level (reject on insert)

Today: don't decide. Tomorrow you'll pick one and implement it.
Today's tests should be **agnostic** about which choice you make —
they just check the public API behavior.

## What changes from the regular Ladder Day shape

Project days are simpler in file layout:
- `app.py` instead of multiple rung files
- `app_test.py` is a single test file growing across three days

The Ladder Day style returns on the next module.
