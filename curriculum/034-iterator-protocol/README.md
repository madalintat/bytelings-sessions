---
day: 034-iterator-protocol
phase: phase-2-pythonic-tools
module: module-06-comprehensions-iterators-generators
style: build-it
---
# Day 34 — Pretend `for` doesn't exist. Build it.

Every Python `for` loop, every `list(...)`, every `*unpack`, every
comprehension — under the hood, all of them speak the same two-method
protocol. Once you've seen it, the language gets smaller.

## The protocol

An object is **iterable** if it has `__iter__()`, which returns an
**iterator**. An iterator has `__next__()`, which returns the next
value or raises `StopIteration`.

That's it. Two methods. The whole tower of Python's looping rests on them.

```python
class Countdown:
    def __init__(self, start):
        self.n = start

    def __iter__(self):
        return self  # Countdown IS its own iterator

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1

for x in Countdown(3):
    print(x)        # 3, 2, 1
```

`for x in obj:` is exactly:

```python
it = iter(obj)              # calls obj.__iter__()
while True:
    try:
        x = next(it)        # calls it.__next__()
    except StopIteration:
        break
    # ... loop body ...
```

Knowing this, you can build your own iterables for any data shape — a
log file you stream, a paginated API, a tree you walk depth-first.

## Iterable vs iterator: the distinction that matters

- **Iterable**: has `__iter__`. A `list`, a `dict`, a `range`. You can
  iterate it many times — each `iter(it)` returns a fresh iterator.
- **Iterator**: has `__next__` (and conventionally `__iter__` returning
  self). Single-use. After `StopIteration`, it's done forever.

`list` is iterable but not an iterator. `iter(my_list)` is an iterator.

```python
nums = [1, 2, 3]
it = iter(nums)
next(it)        # 1
next(it)        # 2
list(it)        # [3]  — the rest, then exhausted
list(it)        # []   — gone
list(nums)      # [1, 2, 3]  — the original list is fine
```

This is why you can `for ... in some_list` twice, but a generator
expression only once. The list is iterable; the generator IS the iterator.

## Why this matters in real code

When you write a class that wraps streaming data — a CSV reader, a DB
cursor, a paginated client — implementing `__iter__` and `__next__`
makes your object work in `for` loops, list comprehensions, `sum`,
`any`, unpacking, everywhere. You don't add API; you add behavior.

## Now: open `fluency.py`

A class is missing one of the two methods. Add it.
