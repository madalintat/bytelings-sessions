---
day: day-107-two-pointer-pattern
phase: phase-5-algorithms
module: module-22-two-pointer-sliding-window-prefix
style: metaphor
---
# Day 107 — Two readers, one book

Imagine two friends reading the same book. One starts at page 1 and
moves forward. The other starts at the last page and moves backward.
At each step, both glance at their current page, decide what to do,
and move on. They stop when they meet in the middle.

That's the two-pointer pattern. One index walks one way, the other
walks the other way, and they coordinate.

## A canonical example: pair-sum on a sorted list

Find a pair of numbers in a sorted list that sum to `target`.

```python
def has_pair(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        s = arr[lo] + arr[hi]
        if s == target: return True
        if s < target:  lo += 1   # need bigger sum, move left pointer right
        else:           hi -= 1   # need smaller sum, move right pointer left
    return False
```

Brute force is O(n²): two loops, every pair. The two-pointer trick is
O(n): each index walks at most n positions, total work 2n.

The whole thing rests on **monotonicity**. The list is sorted. Moving
`lo` right *only* increases the sum. Moving `hi` left *only* decreases
it. So when the sum is too small, you know which pointer to move.
The decision is forced — no search.

## The "opposite ends" pattern

```text
[ . . . . . . . . . . . . . . ]
  ↑                          ↑
  lo                         hi
  →                          ←
```

Use it when:
- The data is **sorted** (or has some other monotonic property).
- You're looking for a **pair** of elements that satisfy a condition.
- Each step, you can decide which pointer to move based on the current
  pair.

Real-world recognition:

- **Pair sum, triplet sum** — classic interview problems, but also
  real: "find two transactions that net to zero" in financial recon.
- **Reverse a string in place** — `lo`, `hi`, swap, walk inward.
- **Palindrome check** — same shape, but compare instead of swap.
- **Merging two sorted streams** — both pointers march forward, you
  pick the smaller head each step. (Yesterday's `merge` was this.)
- **Container with most water** (LeetCode classic) — same pattern.

## The "fast and slow" cousin

A second flavor of two-pointer uses both indices at the *same* end,
moving at different speeds. Classic uses:

- **Cycle detection in linked lists** — Floyd's tortoise and hare.
- **Find the middle of a list** — slow goes 1 step per loop, fast
  goes 2; when fast hits the end, slow is at the middle.
- **Remove duplicates in place** — slow tracks "next write
  position," fast scans ahead.

Same idea (two indices coordinating), different shape.

## How to recognize it in the wild

When you find yourself reaching for a nested loop on a sorted (or
sortable) collection, *ask*: "Can I move two indices toward each
other instead?" If the data has any monotonic structure, the answer
is usually yes — and the runtime drops from n² to n.

## Now: open `fluency.py`

A two-pointer reverse is moving the wrong pointer. Find it.
