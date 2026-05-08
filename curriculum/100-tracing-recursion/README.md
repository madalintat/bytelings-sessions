---
day: day-100-tracing-recursion
phase: phase-5-algorithms
module: module-20-recursion
style: trace
---
# Day 100 — Trace this: predict every return value

Yesterday you learned the *shape* of recursion. Today you trace it.

Look at this function. Predict what each call returns *before* you run
anything.

```python
def f(n):
    if n <= 1:
        return n
    return f(n - 1) + f(n - 2)

print(f(0))  # ?
print(f(1))  # ?
print(f(2))  # ?
print(f(3))  # ?
print(f(4))  # ?
```

Did you guess?

```text
0
1
1
2
3
```

That's Fibonacci. Now trace `f(4)` by hand. Each call spawns two more
calls, like a branching tree:

```text
f(4)
├── f(3)
│   ├── f(2)
│   │   ├── f(1) → 1
│   │   └── f(0) → 0
│   │   (2 returns 1)
│   └── f(1) → 1
│   (3 returns 2)
└── f(2)
    ├── f(1) → 1
    └── f(0) → 0
    (2 returns 1)
(4 returns 3)
```

Notice `f(2)` was computed **twice**. `f(1)` was computed **three**
times. This is why naive Fibonacci is exponentially slow — and a
preview of why memoization (Module 24) exists.

## The mental model: return values bubble *up*

Every recursive call must finish before the call that made it can
finish. Reads like a simple line, but it's the whole game:

1. Call goes down the tree, building a stack of pending work.
2. A base case returns a real value.
3. That value bubbles up, getting combined with siblings via the
   recursive case's expression (`f(n-1) + f(n-2)`).
4. The original call returns once *all* descendants have returned.

When you trace a recursive function, the order to read it is:
**deepest first, then bubble up**. If you read top-to-bottom you'll
get lost.

## A subtler trace: where does the work happen?

```python
def shout(words):
    if not words:
        return
    print(words[0].upper())   # work BEFORE the recursive call
    shout(words[1:])

def shout_back(words):
    if not words:
        return
    shout_back(words[1:])
    print(words[0].upper())   # work AFTER the recursive call
```

`shout(["a", "b", "c"])` prints `A B C`. `shout_back(["a", "b", "c"])`
prints `C B A`. Same recursion shape; one prints before recursing
(forward) and one prints after (reverse). This is the difference
between pre-order and post-order traversal in tree algorithms — same
trick, fancier name.

## Now: open `02_fluency.py`

Two recursive functions print things in a specific order. Read them
carefully and guess the output. Then run.
