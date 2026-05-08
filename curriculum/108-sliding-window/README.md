---
day: 108-sliding-window
phase: phase-5-algorithms
module: module-22-two-pointer-sliding-window-prefix
style: pain
---
# Day 108 — When the obvious solution is O(n × k)

You have a list of 10,000 daily revenue numbers. Marketing asks: "for
every 30-day window, what's the max revenue?" You write the obvious
thing:

```python
def max_per_window(arr, k):
    out = []
    for i in range(len(arr) - k + 1):
        out.append(max(arr[i:i + k]))   # ← look at this
    return out
```

It works. It's also embarrassing — you scan k elements for every one
of the (n - k + 1) windows. That's O(n × k). With n = 10,000 and
k = 30 you do 300,000 comparisons per call. Slow per call, lethal in
a loop.

You feel the pain when the dataset hits a million rows.

## The fix: don't recompute. Slide.

Each window differs from the previous one by exactly two elements:
the one falling off the left, and the one entering from the right.
You shouldn't redo the work in between.

For **sum** windows the optimization is dead simple:

```python
def sum_per_window(arr, k):
    out = []
    s = sum(arr[:k])              # one O(k) cost up front
    out.append(s)
    for i in range(k, len(arr)):
        s += arr[i] - arr[i - k]  # add the new, drop the old
        out.append(s)
    return out
```

That's O(n) total. One subtraction and one addition per slide.

## Sliding window, in two flavors

The pattern splits into two:

**Fixed-size window.** k is given. You know exactly which elements
enter and leave each step. The "running sum / running average / max
in last k" family.

**Variable-size window.** You grow the right edge while a condition
holds; you shrink the left edge when it stops. Classic uses:

- "Longest substring without repeating characters."
- "Smallest subarray with sum >= X."
- "Longest run of 1s if you can flip at most k zeros."

The shape is always:

```python
left = 0
for right in range(len(arr)):
    # add arr[right] to whatever you're tracking
    while invariant_violated:
        # remove arr[left] from your tracking
        left += 1
    # window [left..right] now satisfies the invariant
    update_answer()
```

The pointer `right` moves through the array exactly once. The pointer
`left` also moves through it exactly once (it never goes backward).
That's why this is O(n) not O(n²) — even though there's a `while`
inside the `for`, total moves of `left` is bounded by n.

## WHEN you reach for sliding window

The trigger phrase is **"in every contiguous subarray of length k"**
or **"in some contiguous subarray with property P"**. If you see
"contiguous" + "subarray/substring" + a question about counts,
sums, or max/min, this is your tool.

Real-world hits: rolling-average analytics, rate-limiting (requests
in the last 60s), monitoring (max latency in the last N samples), log
parsing ("longest stretch with no errors"), gene-sequence matching.

## Now: open `fluency.py`

A sliding-sum that recomputes every window. Convert it to slide.
