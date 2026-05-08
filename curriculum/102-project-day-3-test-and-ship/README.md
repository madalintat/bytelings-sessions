---
day: day-098-project-day-3-test-and-ship
phase: phase-4-data-structures
module: phase-4-project-tiny-database
style: story
---
# Day 98 — Project Day 3: test and ship

The table works. Yesterday's test.py is green. Today is the day you
turn "passes the tests we thought of" into "passes tests we didn't
think of." That distinction is what separates code that *works on
my laptop* from code you'd actually deploy.

## Three things to do today

1. **Property tests** — let the test runner generate inputs you
   wouldn't have written by hand.
2. **Brute-force oracle** — compare the indexed table to a naive
   list-of-rows scan on the same workload. They must agree on
   every operation.
3. **A tiny CLI** in `app.py` so you can drive the table from the
   shell.

## The property test pattern

The shape: pick a workload of random ops (insert / delete / get /
range), run them through the indexed `Table` AND through a naive
`ListTable`, and assert their answers match at every step.

```python
def test_oracle_random_workload():
    rng = random.Random(0)
    real = Table()
    oracle = ListTable()  # naive O(n) implementation, in test.py
    for _ in range(500):
        op = rng.choice(["insert", "get", "delete", "range"])
        if op == "insert":
            rk = rng.randint(0, 100)
            real_id = real.insert(rk, {"x": _})
            oracle_id = oracle.insert(rk, {"x": _})
            assert real_id == oracle_id   # same id allocation
        elif op == "get":
            rid = rng.randint(1, 100)
            assert real.get(rid) == oracle.get(rid)
        elif op == "delete":
            rid = rng.randint(1, 100)
            assert real.delete(rid) == oracle.delete(rid)
        elif op == "range":
            lo = rng.randint(0, 100)
            hi = lo + rng.randint(0, 50)
            assert real.range_query(lo, hi) == oracle.range_query(lo, hi)
```

The naive `ListTable` is *not* what we shipped — it's the **oracle**:
slow but obviously correct. If anything they disagree on, the bug is
in the indexed implementation. This pattern catches whole categories
of bugs property-test style without you having to imagine them.

## A tiny CLI in `app.py`

If `__name__ == "__main__"`, read commands from stdin:

```
> insert 30 {"name": "alice"}
1
> get 1
{"id": 1, "range_key": 30, "name": "alice"}
> range 0 100
1: alice
> quit
```

This isn't graded, just useful: now you can poke the database from
the shell and feel it work.

## What "ship" means here

- All tests green.
- Both Day 1 and Day 2 directories' tests still green.
- A README.md inside `phase-4-project-tiny-database/` that explains
  what was built and how to run it. (You wrote this on Day 1 —
  update it now with whatever changed.)
- One paragraph in your project notes (or just in your head): "if I
  were extending this to support a third index type — say, a
  full-text search index over a string column — what would I need
  to change?" The answer is: only `insert` and `delete`. Range
  scans and gets stay the same. That's the test of a clean design.

## What you'll keep from this project

- The dict + linked-list pattern from the LRU. (You didn't use it
  here directly, but it's the same shape: index + storage.)
- The BST + range-aware traversal.
- The discipline of "centralize mutations." It scales from this 100-
  line project to enterprise codebases.

## Now: open `app_test.py`

A property-test scaffold + brute-force oracle is set up. Your job is
to fill in the last few helpers and watch your `Table` agree with the
oracle on a few thousand random operations.
