---
day: 016-linear-search-and-counting-ops
phase: phase-1-python-core
module: module-03-lists-and-counting
style: build-it
---
# Day 16 — Pretend `in` doesn't exist

Imagine Python doesn't ship with the `in` operator. Imagine you have
to write "is this value in this list?" yourself. You'd write something
like this:

```python
def contains(items, target):
    for x in items:           # 1 step per item
        if x == target:       # 1 comparison per step
            return True
    return False
```

That's a **linear search**. The reason it's called linear is the
counting argument:

- Best case: target is at index 0. **1** comparison.
- Worst case: target is at the end, or absent. **n** comparisons.
- Average (uniform random): **n/2** comparisons.

We say "linear search runs in O(n) time" because the worst-case work
grows in proportion to the input size. Constants don't matter for
Big-O — n/2 and n and 100n all collapse to O(n).

## What `in` actually does

For lists, `target in items` runs a linear scan in C. Same algorithm,
faster constants. Same Big-O. So yes, every `if x in big_list:` you
write is paying O(len(big_list)).

If you do that *inside another loop*, you've built an **O(n²)** loop
without noticing. That's the most common Python performance bug:

```python
def common(a, b):
    out = []
    for x in a:
        if x in b:        # ← linear over b each iteration
            out.append(x)
    return out
```

For `len(a) == len(b) == n`, this does ~n² comparisons. The fix is
Day 19 (sets give you O(1) membership). But you can't reach for the
fix until you can *see* the problem.

## Counting ops by hand: the practice

Take a function and count comparisons or assignments as a function of
input size n:

```python
def find_max(xs):
    best = xs[0]              # 1 assignment
    for x in xs[1:]:          # n-1 iterations
        if x > best:          # 1 compare each
            best = x          # ≤1 assignment each
    return best
```

Total: about `2n - 1` operations. Linear in n. **O(n)**.

```python
def has_duplicate_naive(xs):
    for i in range(len(xs)):
        for j in range(len(xs)):
            if i != j and xs[i] == xs[j]:
                return True
    return False
```

Two nested loops over the same list: roughly `n²` comparisons. **O(n²)**.
(Even with early exit; the worst case is when there's no duplicate.)

## Build-it: linear search by hand

Today's drill is to *write* `find_first` and `count_matches` from
scratch. Don't reach for `.index` or `.count` — you'll see how they
work. Tomorrow we name what we just built: that's Big-O.

## Now: open `fluency.py`

Three small linear-scan helpers. Some are wrong, some are slow. Fix
both kinds.
