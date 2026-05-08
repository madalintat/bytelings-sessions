---
day: day-035-yield-and-lazy-evaluation
phase: phase-2-pythonic-tools
module: module-06-comprehensions-iterators-generators
style: trace
---
# Day 35 — Trace this: when does the function actually run?

Predict every line of output *before* you run it.

```python
def chatty():
    print("A: enter")
    yield 1
    print("B: after first yield")
    yield 2
    print("C: after second yield")

g = chatty()
print("--made the generator--")
print(next(g))
print(next(g))
print("--about to ask for one more--")
print(next(g, "DONE"))
```

Did you guess?

```text
--made the generator--
A: enter
1
B: after first yield
2
--about to ask for one more--
C: after second yield
DONE
```

The trick: calling `chatty()` did **not** run the body. It returned a
generator object, paused at the very top. Only the first `next(g)` made
the body start. It ran until it hit `yield 1`, then paused there. The
next `next(g)` resumed, printed `B`, ran until `yield 2`, paused.

When `next` runs off the end, the generator raises `StopIteration` —
the two-argument form of `next` swallows that and returns the default.

## The mental model

- A `def` with `yield` inside is a **generator function**. Calling it
  does not run the body — it builds a paused generator object.
- Each `next(gen)` runs from the current pause point until the next
  `yield`, then pauses again.
- When the function returns (or falls off the end), `StopIteration`
  fires.
- State between yields is preserved automatically. Local variables
  carry across pauses.

This gives you iteration with the ergonomics of writing a normal function:

```python
def take_until(predicate, source):
    for item in source:
        if predicate(item):
            return
        yield item
```

No class, no `__next__`, no `StopIteration` to raise by hand. The
runtime does the bookkeeping.

## `yield from`

When you want to yield every item from another iterable, `yield from`
is shorthand for the obvious loop:

```python
def chain(*iterables):
    for it in iterables:
        yield from it     # equivalent to: for x in it: yield x
```

It also forwards `send`, `throw`, and the iterator's return value, but
99% of the time the loop intuition is enough.

## Now: open `fluency.py`

Two generator functions to fix — both have the right shape but wrong details.
