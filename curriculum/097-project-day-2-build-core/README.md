---
day: day-097-project-day-2-build-core
phase: phase-4-data-structures
module: phase-4-project-tiny-database
style: story
---
# Day 97 — Project Day 2: build the core

Yesterday you stubbed the `Table`. Today you implement it. The
interface tests from Day 1 should all be green by end of session.

## What you'll build

The five public methods, working end to end:

```
insert(range_key, payload) -> int
get(row_id)                -> row dict or None
delete(row_id)             -> bool
range_query(lo, hi)        -> list of rows, sorted ascending
__len__()
```

## The data layout

Two indices, one underlying storage:

```
self._by_id:    dict[int, dict]      # id -> row dict
self._by_range: BST keyed by (range_key, id)
```

Why `(range_key, id)` tuples in the BST? It handles **duplicate
range_keys for free**. Two rows with `range_key=30` get distinct keys
`(30, id_a)` and `(30, id_b)` — same first slot, different second
slot. The BST orders them naturally; the in-order traversal yields
them ascending; range queries return both.

The BST node stores the tuple as its value. The BST is a *set* over
those tuples. To answer `range_query(lo, hi)`, you walk the BST and
emit every entry whose first slot is in `[lo, hi]`. Then for each
emitted tuple, look up the row in `self._by_id`.

## The "stay in sync" rule

Both indices change on every insert and delete. Make `insert` and
`delete` the **only two methods** that mutate the table. Everything
else is read-only. This is the tightest invariant a database has,
and the easiest to break: a one-line shortcut that updates `_by_id`
but forgets `_by_range` is a guaranteed bug that won't show up
until a range_query happens to touch the affected row.

## A copy of the BST you wrote on Day 89

You'll need a small BST. Copy the one from Day 89, or use a
lightweight version in `app.py` directly. The methods you'll need:

- `insert(value)` (idempotent — duplicates already filtered if your
  values are unique tuples)
- `delete(value)`
- a way to iterate values in-order, OR a `range_query(lo_key, hi_key)`
  that walks only the relevant subtrees

For this project, an inorder traversal that filters on range_key is
fine. The point is to *use* the BST, not optimize it further.

## Today's deliverable

`app.py` complete. All Day 1 tests pass. Your `app_test.py` for today
adds a few more targeted tests:

- delete touches both indices (insert two rows with same range_key,
  delete one, check the other is still in `range_query`)
- range_query is `[lo, hi]` inclusive on both ends
- update via delete+insert: shape of the table after a "swap"

If you finish early, start sketching the property-based tests for
tomorrow.

## Now: write the implementation

`app_test.py` is set up to run against `app.py`. Use the watcher; iterate.
