---
day: day-081-queue-and-why-list-queue-is-slow
phase: phase-4-data-structures
module: module-16-stacks-queues-deques
style: pain
---
# Day 81 — The queue you wrote with `list` is secretly O(n)

You need a queue: first in, first out. Print jobs. Tasks. Customers.
Whatever's been waiting longest goes next. The natural sketch in
Python is a list — push to the end, pop from the front:

```python
queue: list = []
queue.append("alice")
queue.append("bob")
queue.pop(0)   # "alice" — looks fine
```

Ship it. Six months later, your background-task processor handles
50,000 queued jobs and runs slower than the box that handles 5,000.
You profile it. Most of the time is spent in `list.pop(0)`.

## Why it's slow

A Python `list` is a contiguous array of pointers. `list.append` puts
a value at the *end*, where there's already room reserved — O(1)
amortized. But `list.pop(0)` removes the *front*, then has to **shift
every other element one slot left** so the next index 0 is correct.
That's O(n). Same problem with `list.insert(0, x)`.

Push 50,000 items, pop them all from the front, you've done about
1.25 billion shifts. That's why the queue lagged.

## The fix: `collections.deque`

A **deque** (pronounced "deck") is a doubly-ended queue. It's
implemented as a doubly-linked list of fixed-size blocks, so adds and
removes at *both* ends are O(1). The standard library ships one:

```python
from collections import deque

q: deque = deque()
q.append("alice")    # enqueue
q.append("bob")
q.popleft()          # "alice" — O(1) instead of O(n)
```

`append` puts on the right, `popleft` takes from the left. That's a
queue. `appendleft` and `pop` give you a stack-on-the-other-end too —
that's why it's a *deque*.

## When to use which

| Need | Use | Why |
|---|---|---|
| Stack (LIFO) | `list` | `append` + `pop()` — both O(1), no overhead |
| Queue (FIFO) | `deque` | `append` + `popleft()` — both O(1) |
| Both ends | `deque` | only structure that supports both fast |
| Random index access | `list` | `deque` is O(n) by index |

The trap is that `list` *looks* like it works as a queue. The tests
pass. The code reads fine. The bug is invisible until the data gets
big. This is a recurring shape: **wrong-but-works** is the worst kind
of bug because nothing flags it.

## Building a Queue class

You'll wrap a `deque` in a `Queue` class today, with the same shape as
yesterday's `Stack`: `enqueue`, `dequeue`, `peek`, `len`, `bool`. Same
discipline — empty operations raise a clear `IndexError`.

## Now: open `fluency.py`

A queue is misbehaving. Find the slow line and the wrong-end line.
