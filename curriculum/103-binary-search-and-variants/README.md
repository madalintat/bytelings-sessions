---
day: day-103-binary-search-and-variants
phase: phase-5-algorithms
module: module-21-searching-sorting
style: build-it
---
# Day 103 — Pretend `bisect` doesn't exist

Python ships a perfectly good binary-search module called `bisect`.
Today you're going to ignore it. The point isn't "find the target."
The point is to feel why halving works.

## The setup

You have a sorted list of 1,000,000 ints. You want to know if `target`
is in it. The naive approach scans linearly: ~1,000,000 comparisons.
Binary search: ~20.

Two-zero. Twenty. That's the gap between "good enough for tiny lists"
and "instantaneous on a million."

## Build it

```python
def bsearch(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1   # target must be to the right
        else:
            hi = mid - 1   # target must be to the left
    return -1
```

The whole algorithm is "look at the middle. Eliminate half." Three
things that matter:

1. **`lo <= hi`, not `lo < hi`.** The single-element case (`lo == hi`)
   still needs to be checked.
2. **`mid + 1` and `mid - 1`.** You already checked `mid`, so don't
   include it in the next half. Forget this and you get an infinite
   loop.
3. **Sorted input is required.** Binary search on unsorted data is
   nonsense. If you sort first, you've spent O(n log n) — only worth
   it if you're searching the same array many times.

## The two variants you'll actually use

You rarely need "exact match." Far more often you need:

- **Lower bound** — the first index where `arr[i] >= target`. The
  insertion point that keeps the list sorted.
- **Upper bound** — the first index where `arr[i] > target`. Useful
  for counting duplicates: `upper(arr, x) - lower(arr, x)`.

Both have the same shape as `bsearch` — the only thing that changes
is the comparison and what you return at the end (the `lo` after the
loop, not `-1`).

## WHEN to reach for binary search

Real-world recognition is the goal. You should think "binary search"
the moment you see one of these:

- **A sorted array, repeated lookups.** Logs sorted by timestamp,
  finding all entries between 9:00 and 10:00. Two binary searches
  bound the slice.
- **"First X where condition is true."** If the condition is
  *monotonic* — once it flips from false to true it stays true — you
  can binary-search the boundary. ("First version of the build that
  passes" — git bisect.)
- **Numerical answer with a yes/no test.** "What's the smallest X
  such that f(X) is at least 100?" Binary-search over X. This is
  surprisingly common in scheduling, capacity planning, and
  competitive coding.

If your data is unsorted and only used once, don't bother — just scan.

## Now: open `02_fluency.py`

A binary search with a classic off-by-one. Find it.
