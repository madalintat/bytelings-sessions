---
day: day-091-heap-invariant-and-heapq
phase: phase-4-data-structures
module: module-19-heaps-and-hash-tables
style: tour
---
# Day 91 — A tour of `heapq` (and the invariant under it)

You need a structure that always gives you the minimum, fast — but
also lets you add new items, fast. You don't need full sorted order;
you only need the smallest. **A heap** is for exactly that.

```python
import heapq
h: list[int] = []
heapq.heappush(h, 5)
heapq.heappush(h, 1)
heapq.heappush(h, 3)
heapq.heappop(h)   # 1
heapq.heappop(h)   # 3
```

Under the hood, that list is laid out so the smallest item is always
at index 0. Push and pop are O(log n). Peek (`h[0]`) is O(1). And
the data structure is just... a Python list. No fancy class.

## The invariant

A **min-heap** is a complete binary tree in which every parent's
value is ≤ both its children. (A max-heap has ≥ — same shape, flipped
comparison.) "Complete" means every level is full except the last,
which is filled left-to-right. That shape lets us flatten the tree
into an array with a clean rule:

```
index:    0  1  2  3  4  5  6
values:   1  3  5  4  7  9  6     (a valid min-heap)

         tree:
                 1
                / \
               3   5
              / \ / \
             4  7 9  6
```

For node at index `i`:
- parent = `(i - 1) // 2`
- left child = `2*i + 1`
- right child = `2*i + 2`

The root is at index 0. The smallest item is *always* at index 0 —
that's what "min-heap" means. Anything you do (push, pop) has to
restore that invariant.

## What `heapq` gives you

```python
heapq.heappush(h, x)        # add x, O(log n)
heapq.heappop(h)            # pop smallest, O(log n)
h[0]                        # peek smallest, O(1)
heapq.heapify(lst)          # turn an arbitrary list into a heap, O(n) (!)
heapq.heappushpop(h, x)     # push then pop, in one step (faster)
heapq.heapreplace(h, x)     # pop then push, in one step
heapq.nsmallest(k, iterable)
heapq.nlargest(k, iterable)
heapq.merge(*iterables)     # merge sorted iterables lazily
```

Two surprises worth memorizing:
- **`heapify` is O(n), not O(n log n).** Sift-down from the middle
  out is cheaper than n separate pushes. Use it whenever you have
  the data up front.
- **`nsmallest` / `nlargest` are O(n log k)**, beating sorting when
  k is small. The classic "top-k" answer.

## When to reach for a heap

- **Top-k** something — busiest IPs, biggest files, smallest k items
  — when k is much smaller than n.
- **Priority queue** — process events in order of urgency, not order
  of arrival.
- **k-way merge** — merge k sorted streams; each step picks the
  smallest of k heads, which is what a heap is for.
- **Schedulers** — "next job is the one with the earliest start
  time."

If you need *all* items in sorted order, just sort. Heaps are for
"give me the next one, repeatedly."

## Python heaps are min-heaps. To get max:

Negate values on push, negate them back on pop. Or wrap them in a
`(priority, item)` tuple where `priority = -score`. There's no
built-in max-heap.

## Now: open `02_fluency.py`

Two heap idioms have one bug each.
