---
day: 109-prefix-sums
phase: phase-5-algorithms
module: module-22-two-pointer-sliding-window-prefix
style: build-it
---
# Day 109 — Build a "any range, instant sum" data structure

You receive a list of daily site visits. Your dashboard asks 100,000
questions: "what's the total for days 14 to 88?" "Days 200 to 250?"
"Days 1 to 365?" Each query is a slice-sum.

The naive answer is `sum(visits[a:b])` — O(b - a) per query, up to
O(n) each. With 100,000 queries on a million-day list, that's 10^11
operations. Your dashboard times out.

You need O(1) per query. Pretend Python doesn't have any helper.
Build it from scratch.

## The trick: precompute one extra array

```python
def build_prefix(arr):
    p = [0]                  # p[0] is 0; the empty-prefix sum
    for x in arr:
        p.append(p[-1] + x)
    return p                 # len(p) == len(arr) + 1
```

`p[i]` is "the sum of arr[0..i-1]." So:

```text
arr = [3, 1, 4, 1, 5]
p   = [0, 3, 4, 8, 9, 14]
```

To get the sum of any slice `arr[a:b]`:

```python
def range_sum(p, a, b):
    return p[b] - p[a]       # O(1)
```

Read it as: "sum of [0..b) minus sum of [0..a)." What's left is
exactly `arr[a..b)`. Building `p` is O(n) once. Every query
afterward is one subtraction.

## The general principle: O(1) queries via precompute

Prefix sums are the *simplest* example of a much bigger idea:
**spend O(n) ahead of time so each query is O(1)**. You'll see this
pattern again and again:

- **Cumulative counts** — same shape, but tracking how many things
  fall under each bucket.
- **2D prefix sums** — for "sum of submatrix" in image processing
  and computer vision (called "summed-area tables" there).
- **Prefix XOR** — useful for "XOR of any range" queries.
- **Hashes / fingerprints** — rolling hashes use a related trick.

## Where prefix sums shine in interviews and reality

Two problems where prefix sums *are* the answer:

**1. Subarray with given sum.** "Does any contiguous subarray sum to
exactly k?" Build prefix sums, walk through them, and at each `p[i]`
check whether `p[i] - k` has appeared before (in a hash set). O(n).
This works for *negative* numbers too, where sliding window doesn't.

```python
def has_subarray_sum(arr, k):
    seen = {0}
    s = 0
    for x in arr:
        s += x
        if s - k in seen:
            return True
        seen.add(s)
    return False
```

**2. Rolling difference.** Logs that record cumulative counts (visits
this hour, requests served, etc.) are essentially prefix sums
already. To recover per-period values you take differences. Lots of
real telemetry comes pre-prefixed for exactly this reason.

## WHEN to think prefix sums

The trigger phrase is **"sum (or count) over many ranges of the same
fixed array"**. Especially when:

- The array doesn't change between queries.
- You'll do many queries (otherwise just sum the slice).
- The values can be *anything* — sliding window stops working with
  negatives, prefix sums don't care.

For mutable arrays with range queries, you'd reach for a Fenwick
tree or segment tree (out of scope here). For static arrays, prefix
sums are the simplest possible answer.

## Now: open `fluency.py`

A range-sum function with an off-by-one. Find it.
