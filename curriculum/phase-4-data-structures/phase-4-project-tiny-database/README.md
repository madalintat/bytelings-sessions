# Phase 4 Project — Tiny In-Memory Database

A 3-day project that welds the four data structures from this phase
into one small, useful tool: an in-memory table with two indices —
a **hash index** for equality lookups and a **BST index** for range
queries.

## The Scenario

You're building the cache layer in front of a slow analytics service.
Customers fire two kinds of queries at it all day:

- "give me the row where `id == 4815`"  (point lookup)
- "give me every row where `age >= 30 AND age <= 40`"  (range scan)

A list-of-rows would do both, in O(n). For this many rows, that's not
fast enough. You'll build a tiny `Table` class that stores rows once
but keeps two **indices** pointing into the storage:

- A `dict`-like **hash index** on the equality column → O(1) point
  lookup.
- A **BST index** on the range column → O(k + log n) range scan.

Each index points to row IDs (or row references), not copies. Updates
go through the table API and keep both indices in sync.

## Concepts checklist

This project deliberately exercises the whole phase:

- [x] **Hash table** — for the equality index. (M19)
- [x] **BST** — for the range index. (M18)
- [x] **In-order traversal** — to deliver range results in sorted
      order. (M18)
- [x] **Linked list / deque** — for storage of rows + a small write
      buffer (optional). (M16/M17)
- [x] **Recursion + tree thinking** — through the BST insert/delete.
- [x] **Big-O reasoning** — measuring point vs range vs naive scan.

## Day-by-day plan

### Day 1 — Design and scaffold

Sketch the API: what does the `Table` look like? What methods does it
expose? Pick a row representation (`dict`? a tuple? a small dataclass-
like object?). Decide which column is the hash key and which is the
range key. Stub out the class with a `dict` for the hash index and a
BST for the range index. Write the *interface* tests first; let them
fail. Don't implement yet.

### Day 2 — Build core

Implement `insert`, `get_by_id`, `range_query`, and `delete`. Both
indices must stay in sync — every insert touches both, every delete
touches both. Write code defensively: assertions in development that
the indices match the underlying storage.

### Day 3 — Test, polish, ship

Property-based tests: insert N random rows, then run a sequence of
random gets / range queries / deletes; the two indices must always
report the same answer as a brute-force scan. Profile against a
list-of-rows brute force baseline; you should see point-lookup go
from O(n) to O(1) and range scan get a measurable win. Write the
README in the project folder explaining how to use it.

## Graduated hints (open only if stuck)

<details>
<summary>Stuck on row IDs?</summary>

Use an auto-incrementing integer; the table maintains `self._next_id`.
The hash index maps `id -> row_object`, the BST index maps
`range_key -> set_of_ids` (because multiple rows can share a range
value).
</details>

<details>
<summary>Stuck on range BST returning duplicates?</summary>

If your range column has duplicates, store row IDs in a `set` at each
BST node, not a single value. Or store `(range_value, row_id)` tuples
and let normal BST ordering handle ties via the second slot.
</details>

<details>
<summary>Stuck on staying in sync?</summary>

Centralize the writes. Make `insert(row)` and `delete(id)` the *only*
two methods that mutate state. Both methods touch both indices.
Anywhere else that wants to mutate must go through them.
</details>

## Stretch goals

- Add a third index type: a sorted list, and benchmark all three on
  range queries.
- Persist the table to disk as JSON; re-build the indices on load.
- Add a tiny CLI that takes a config file and serves an interactive
  REPL.

## Self-evaluation rubric

Before you call it done:

- [ ] `pytest` passes for all three project days.
- [ ] You can explain *out loud* why point lookup is O(1) and range
      query is O(k + log n) on a balanced tree.
- [ ] `delete(id)` removes the row from BOTH indices. Test for it.
- [ ] You have a benchmark script (or a small note) showing the
      lookup speedup vs a naive list scan.
- [ ] You'd be comfortable extending this with a third index type
      without breaking the existing two.
