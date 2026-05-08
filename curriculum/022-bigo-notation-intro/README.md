---
day: 022-bigo-notation-intro
phase: phase-1-python-core
module: module-04-hashing-dicts-sets-and-bigo
style: compare
---
# Day 22 — Two ways to count duplicates

You need to find out whether a list has any duplicates. Two snippets:

### Snippet A
```python
def has_dup_a(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False
```

### Snippet B
```python
def has_dup_b(items):
    seen = set()
    for x in items:
        if x in seen:
            return True
        seen.add(x)
    return False
```

Both return correct answers. Which is faster, and *how do we say it
without measuring*?

## Counting work as a function of n

Let `n = len(items)`.

- **A:** outer loop runs n times. Inner loop runs at most n times. The
  total comparisons in the worst case (no duplicates) are
  `(n-1) + (n-2) + ... + 1 = n(n-1)/2`. That's about **½ n²**.
- **B:** outer loop runs n times. Each step does one set membership
  test (O(1) on average — Day 21 proves this) and one set insert (also
  O(1)). Total work: **about n**.

For small n (say 10), B's win is invisible. For n = 1,000,000:
- A does ~500 billion comparisons.
- B does ~1 million.

That's the difference between "instant" and "go get coffee."

## What Big-O is, in one paragraph

Big-O is the **shape** of how work grows when input grows. We drop:

1. **Constants:** `3n + 5` and `n` are both **O(n)**. They differ by a
   factor that doesn't matter as n → ∞.
2. **Lower-order terms:** `n² + n` is **O(n²)**. The square term wins
   for large n.

What's left is the *family* of growth: O(1), O(log n), O(n),
O(n log n), O(n²), O(2ⁿ). Each is dramatically slower than the one
before, in a way that compounds.

## A pocket reference

| Big-O | Name | Example |
|---|---|---|
| O(1) | constant | `lst[i]`, `dict[key]`, `len(lst)` |
| O(log n) | logarithmic | binary search (Phase 5) |
| O(n) | linear | linear search, sum, max |
| O(n log n) | linearithmic | `sorted()`, merge sort |
| O(n²) | quadratic | nested loop over same data |
| O(2ⁿ) | exponential | naive subset / fib recursion |

## Three rules of thumb

1. **A loop over n items is O(n).** Two nested loops over the same n
   items are O(n²).
2. **Sequential code adds; nested code multiplies.** O(n) followed by
   O(n) is O(n + n) = O(n). O(n) inside O(n) is O(n × n) = O(n²).
3. **Find the slowest line in the loop.** If a line takes O(n) and
   you're inside an O(n) loop, the total is O(n²) — even if the rest
   of the loop body is O(1).

Big-O isn't a number, it's a *prediction shape*. By the end of Phase 4,
you'll be sketching it without thinking.

## Now: open `fluency.py`

Compare two pairs of functions. Pick the faster one *and* say its
Big-O.
