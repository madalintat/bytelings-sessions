---
day: day-013-list-slicing-deep
phase: phase-1-python-core
module: module-03-lists-and-bigo
style: trace
---
# Day 13 — Predict each slice

Day 6 trained you on string slicing. Lists work the same — except
they're **mutable**, which unlocks slice-assignment. Walk this trace:

```python
xs = [10, 20, 30, 40, 50]

a = xs[1:4]       # ?
b = xs[:3]        # ?
c = xs[::2]       # ?
d = xs[::-1]      # ?
e = xs[1:]        # ?
f = xs[10:20]     # ?
```

Predict, then check:

- `a` → `[20, 30, 40]`. Half-open interval, same as strings.
- `b` → `[10, 20, 30]`.
- `c` → `[10, 30, 50]`. Step 2.
- `d` → `[50, 40, 30, 20, 10]`. Reversed.
- `e` → `[20, 30, 40, 50]`.
- `f` → `[]`. Out-of-range slices don't raise.

Same shape, same defaults, same negative-step behavior. The interesting
new thing is **slice assignment**.

## Trace this — the part that's *only* legal on lists

```python
xs = [10, 20, 30, 40, 50]

xs[1:3] = [99, 99]     # replace 20, 30 with two 99s
# xs is now [10, 99, 99, 40, 50]

xs[1:3] = [0]          # shrink: replace two slots with one value
# xs is now [10, 0, 40, 50]

xs[1:1] = [1, 2, 3]    # insert without removing
# xs is now [10, 1, 2, 3, 0, 40, 50]

xs[::2] = [-1, -2, -3, -4]   # extended slice assignment — sizes MUST match
# xs is now [-1, 1, -2, 3, -3, 40, -4]

del xs[1:4]            # delete a range in place
# xs is now [-1, -3, 40, -4]
```

Each line is doing in-place mutation. `xs` is the *same list object*
the whole time — only its contents change.

## Slice copy: a shallow copy in three chars

`ys = xs[:]` is the canonical way to make a shallow copy of a list.
"Shallow" means: the outer list is new, but the inner objects are
shared. For nested lists, that matters:

```python
matrix = [[0, 0], [0, 0]]
copy = matrix[:]
copy[0][0] = 99
matrix       # [[99, 0], [0, 0]]   — the inner list is shared!
```

For deep copies of nested data, `import copy; copy.deepcopy(x)`.

## A subtle perf note

Slicing a list creates a new list with `len(slice)` elements. So
`big[:n]` is **O(n)**, not O(1). Don't slice in a hot loop unless
you need the new list. (For "first n items, but lazily," the answer
is `itertools.islice` — Phase 2.)

## Now: open `fluency.py`

Three slice expressions — including a slice *assignment* — are wrong.
Patch them.
