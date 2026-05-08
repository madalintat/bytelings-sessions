---
day: day-105-merge-sort-and-quick-sort
phase: phase-5-algorithms
module: module-21-searching-sorting
style: build-it
---
# Day 105 — Build the two sorts everyone actually means

Yesterday's tour was the warmup. Today you build the two real
divide-and-conquer sorts: **merge sort** and **quicksort**. Both are
O(n log n) on average. Both teach the same lesson — *split, solve
each half, glue back together* — but their personalities differ.

## Merge sort: the steady worker

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(a, b):
    out = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out
```

Three things to internalize:

1. **Base case is "length 0 or 1."** A list of one is already sorted.
2. **The work is in `merge`.** Splitting is free; combining is the
   linear-time pass that, summed across log n levels, gives
   n log n.
3. **`<=` in the comparison gives stable sort.** "Stable" means equal
   keys keep their original order (more on this tomorrow).

Merge sort uses O(n) extra memory (for `out`). Always exactly
O(n log n), best and worst case. No surprises. That's why databases
that need predictable behavior often use it.

## Quicksort: the fast gambler

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)
```

Pick a pivot. Partition into "less," "equal," "greater." Recurse on
the two outer chunks. Stitch back.

Why "gambler"? Because if your pivot is bad — e.g., you always pick
the first element and the input is already sorted — you get O(n²).
With a *random* or *median-of-three* pivot, average is O(n log n)
and you basically never hit the worst case.

Quicksort beats merge sort on cache: it sorts **in place** (with a
tighter implementation than the one above) and touches contiguous
memory. That's why C's `qsort` and many language libraries use it as
the inner workhorse.

## WHEN each one wins

- **Merge sort wins when:** stability matters; you need worst-case
  guarantees; data is on disk in chunks (external merge sort).
- **Quicksort wins when:** you're sorting in memory; cache locality
  matters; you can pick a good pivot.

In practice, you'll almost never write either by hand — Python's
Timsort (next module day) is a hybrid that beats both for general
mixed input. But the *patterns* (divide-and-conquer, partitioning,
merging) recur everywhere: parallel processing splits work this way,
external sorts work this way, MapReduce is "merge sort, distributed."

## Now: open `fluency.py`

A merge function with one bug that only shows up on certain inputs.
Find it.
