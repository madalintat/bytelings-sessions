---
day: day-114-recursion-to-memoization
phase: phase-5-algorithms
module: module-24-dp-greedy-backtracking
style: pain
---
# Day 114 — When Fibonacci is the slowest function you've ever written

Run this:

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(40))   # ...wait, why is my laptop fan spinning up?
```

`fib(40)` takes a couple of seconds. `fib(50)` won't finish before
your meeting. `fib(100)`, you'll be retired.

The pain: this recursion is *exponential*. `fib(n)` makes roughly
2^n calls because the same subproblem is computed over and over. We
saw this in Day 100's trace — `fib(2)` was computed twice in `fib(4)`,
three times in `fib(5)`, eight times in `fib(7)`. By `fib(40)` you've
recomputed `fib(2)` more than 100 million times.

## The fix in three characters

```python
from functools import cache

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

`@cache` (Python 3.9+) memoizes the function: the first time you call
`fib(7)`, the answer is computed and stored; every subsequent call
with `7` is an O(1) lookup. The same recursion that took seconds for
n=40 returns instantly for n=400.

That's all dynamic programming is, in its most useful form: **plain
recursion plus memoization.**

## Why it works: the right shape

DP works when:

1. **Optimal substructure.** The answer to a problem can be built
   from answers to smaller problems. (Fib(n) = fib(n-1) + fib(n-2).)
2. **Overlapping subproblems.** The same smaller problem is asked
   many times. (Without overlap, recursion + memoization is just
   recursion.)

If you have both, memoization turns exponential into polynomial.

## When not to bother

If your recursion has no overlap — like merge sort, where you split
into two completely fresh halves — there's nothing to cache. Adding
`@cache` to merge sort wastes memory and changes nothing.

The litmus test: do `fib(40)`'s subproblems repeat? Hugely. Do merge
sort's? Never. The first benefits, the second doesn't.

## The mental shift

Before this module, recursion is "shrink the problem." Now recursion
is "shrink the problem, *and remember*." That single addition is the
gateway to DP.

You'll write `@cache` more than any other DP technique in real code,
because most of the time you don't need to be fancy. A recursive
solution that's clear, correct, and memoized usually beats a clever
hand-rolled bottom-up table — and is way easier to debug.

## WHEN you reach for memoized recursion

Trigger phrases that should make you reach for `@cache`:

- "How many ways..." (counting paths, partitions, subsets).
- "What's the optimal..." (cost, profit, length) where the answer
  decomposes into a choice plus the optimal of a smaller subproblem.
- "Can I reach..." with a state space that branches.

Examples in the wild: spell-check edit distance, regex matching,
text wrapping (Knuth's word-justification algorithm), dynamic
pricing, optimal binary search trees, RNA secondary structure
prediction in bioinformatics.

If your recursive function takes hashable arguments and computes the
same thing repeatedly, `@cache` is the answer.

## Now: open `fluency.py`

A naive recursive function that's too slow on inputs > 30. Speed it
up with one decorator.
