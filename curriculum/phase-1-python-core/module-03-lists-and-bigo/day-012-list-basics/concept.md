---
day: day-012-list-basics
phase: phase-1-python-core
module: module-03-lists-and-bigo
style: tour
---
# Day 12 — A guided tour of one tiny list

Open this snippet. Read every line. Notice what the list is doing
underneath.

```python
people = ["Alice", "Bob", "Carol"]
people.append("Dave")          # 1
people.insert(0, "Mada")       # 2
first = people[0]              # 3
last  = people[-1]             # 4
people[1] = "Bobby"            # 5  (lists are mutable!)
n = len(people)                # 6
"Alice" in people              # 7  (linear scan)
del people[2]                  # 8
people.remove("Bobby")         # 9  (by value)
last_popped = people.pop()     # 10
```

A line-by-line tour:

1. `append(x)` adds to the **end**. O(1) amortized — fast.
2. `insert(0, x)` adds at the **start**. Every element after has to
   shift right one slot. O(n). For "always insert at the front,"
   reach for `collections.deque` instead (Phase 4).
3. `[0]` indexes from the front. O(1).
4. `[-1]` indexes from the back. Also O(1) — Python translates the
   negative index to `len - 1` directly.
5. **Lists are mutable**: you can replace an element in place. Strings
   can't do this (Day 8). This single fact is the line between "value
   types" and "container types" in Python's mental model.
6. `len(x)` is O(1) for lists; the count is stored on the list.
7. `in` does a **linear scan** until it finds a match. O(n). For
   membership tests on large data, you'll switch to `set` in Day 19.
8. `del lst[i]` removes by index. Shifts everything after. O(n).
9. `lst.remove(v)` removes the first occurrence by value. O(n) — it
   has to find it first, then shift.
10. `pop()` (no arg) removes the **last** element. O(1).
    `pop(0)` removes the first. O(n).

## A list is a heterogeneous, ordered, mutable, growable array

Each word in that sentence matters:

- **Heterogeneous:** `[1, "two", 3.0, None]` is legal. (You usually
  want it to be uniform anyway, for sanity.)
- **Ordered:** insertion order is preserved. `[1, 2]` ≠ `[2, 1]`.
- **Mutable:** in-place edit allowed.
- **Growable:** Python over-allocates the underlying buffer so most
  appends don't need to copy.

## A common gotcha: aliasing

```python
a = [1, 2, 3]
b = a              # b is the same list as a
b.append(4)
a                  # [1, 2, 3, 4]   — surprised?

c = a.copy()       # OR list(a) OR a[:]  — three ways to make a shallow copy
c.append(99)
a                  # unchanged: [1, 2, 3, 4]
```

The `=` doesn't copy a list. It binds another *name* to the same
*object*. Day 4 (names vs values) was building toward this moment.

## Now: open `02_fluency.py`

Three tiny list operations are wrong. Patch them.
