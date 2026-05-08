---
day: 019-set-operations
phase: phase-1-python-core
module: module-04-hashing-dicts-sets-and-bigo
style: compare
---
# Day 19 — List vs set: pick wisely

Two snippets. Both find which usernames in `requested` are NOT yet
in `existing`. Same correct output. Wildly different costs.

### Snippet A — list of strings
```python
def missing_a(requested: list[str], existing: list[str]) -> list[str]:
    out = []
    for r in requested:
        if r not in existing:        # linear scan over `existing`
            out.append(r)
    return out
```

### Snippet B — set membership
```python
def missing_b(requested: list[str], existing: list[str]) -> list[str]:
    have = set(existing)             # one-time O(n) build
    return [r for r in requested if r not in have]
```

For `len(requested) == len(existing) == 1,000,000`:

| | Snippet A | Snippet B |
|---|---|---|
| Setup | none | O(n) |
| Per-lookup | O(n) | O(1) avg |
| Total | O(n²) — minutes | O(n) — milliseconds |

The `set` swap is one of the highest-leverage Python moves you'll
ever make.

## What a `set` is

A set is an **unordered collection of unique hashable elements**. It's
backed by the same hash-table machinery as `dict` (Day 21), so it has
the same performance profile:

- `x in s` — O(1) average
- `s.add(x)`, `s.discard(x)` — O(1)
- `len(s)` — O(1)
- iteration: O(n)

Unlike dicts, sets don't preserve insertion order in the spec (in
practice CPython does, but don't rely on it for sets).

## Set algebra

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # union:        {1, 2, 3, 4, 5, 6}
a & b    # intersection: {3, 4}
a - b    # difference:   {1, 2}        — in a, not in b
a ^ b    # symmetric:    {1, 2, 5, 6}  — in either, not both
```

Same operations exist as methods (`a.union(b)`, `a.intersection(b)`,
`a.difference(b)`, `a.symmetric_difference(b)`). Methods accept any
iterable; operators require both sides to be sets.

## Comparison: when to use what

| Need | Pick |
|---|---|
| Order matters | `list` |
| Indexed access (`[i]`) | `list` |
| Fast membership (`x in s`) | `set` or `dict` |
| Unique items only | `set` |
| Counting / mapping | `dict` |
| Many duplicates allowed | `list` |

**Rule of thumb:** if your only question is "is this in the
collection?", reach for `set`. If you need a key→value map, reach for
`dict`. If you need order or duplicates, reach for `list`.

## A small gotcha

```python
empty_set = {}        # this is an empty DICT, not a set!
empty_set = set()     # canonical empty set
```

`{1, 2, 3}` is a set literal. `{}` is a dict literal. To make an empty
set you must write `set()`.

## Now: open `fluency.py`

Three small functions; pick the right structure.
