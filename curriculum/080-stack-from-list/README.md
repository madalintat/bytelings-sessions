---
day: day-080-stack-from-list
phase: phase-4-data-structures
module: module-16-stacks-queues-deques
style: build-it
---
# Day 80 — A stack, from scratch, in 12 lines

Pretend Python doesn't ship a `Stack` class. (It doesn't, by name.) You
need one anyway: parser undo state, a recursion-killer for tree walks,
a back-button for an editor. So you'll build one.

A **stack** is a last-in, first-out (LIFO) collection. You push to the
top, you pop from the top, you peek at the top. That's the whole API.
The plate-rack metaphor is exact: the last plate you set down is the
first one you pick up.

## When to reach for one

You want a stack any time the *thing you most recently saw* is the
thing you next need to handle:

- Matching opening/closing brackets
- Walking a tree without recursion
- Implementing undo
- Backtracking from a dead end in a search
- Reversing anything

If you ever catch yourself thinking "I need to remember what I just did
so I can come back to it," that's a stack.

## Build it on top of `list`

Python's `list` already supports the two operations you need at the
right end:

```python
stack: list[int] = []
stack.append(10)   # push
stack.append(20)
stack[-1]          # peek -> 20
stack.pop()        # pop -> 20, stack now [10]
```

Both `append` and `pop` (no index) are amortized O(1) — `list` over-
allocates room at the end so most pushes don't have to copy. That's
why a list-backed stack is the right default in Python.

What you should NOT do: `stack.pop(0)` or `stack.insert(0, x)`. Those
are O(n) — every other element shifts. We'll see why that matters
tomorrow when we try to build a queue this way.

## Wrap it in a class anyway

A bare list works, but a `Stack` class makes intent loud at the call
site. `editor.history.push(state)` reads better than
`editor.history.append(state)`. You also get to control the API:
your stack can refuse to pop when empty (raising a clear error) instead
of silently raising `IndexError` from the wrong layer.

```python
class Stack:
    def __init__(self) -> None:
        self._data: list = []
    def push(self, x) -> None:
        self._data.append(x)
    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()
    def peek(self):
        return self._data[-1]
    def __len__(self) -> int:
        return len(self._data)
```

Twelve lines. That's a real data structure.

## Now: open `fluency.py`

Two broken stack helpers to fix.
