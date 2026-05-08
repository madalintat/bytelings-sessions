---
day: day-025-scope-legb-and-closures
phase: phase-1-python-core
module: module-05-functions-closures-decorators
style: trace
---
# Day 25 — Predict each `print`

Read this code top to bottom. **Before each print, predict the output.**

```python
x = "global"

def outer():
    x = "outer"

    def inner():
        x = "inner"
        print(1, x)        # ?
    inner()
    print(2, x)            # ?

outer()
print(3, x)                # ?
```

Predicted? Compare:

- `1 inner` — inside `inner`, the local `x = "inner"` shadows everything.
- `2 outer` — `inner` rebinding `x` only created a *new local* in
  `inner`'s frame; it didn't touch `outer`'s `x`.
- `3 global` — `outer` did the same; it shadowed the module-level `x`
  but didn't change it.

## The rule: LEGB

When Python looks up a name, it searches in this order:

1. **L**ocal — the current function's locals.
2. **E**nclosing — any enclosing function's locals (for nested fns).
3. **G**lobal — the module's top-level names.
4. **B**uilt-in — `len`, `print`, `dict`, etc.

It stops at the first match. Assignment defaults to *Local* — that's
why `x = "inner"` made a new local instead of changing the outer `x`.

## Trace #2: closing over a variable

```python
def make_counter():
    count = 0
    def step():
        nonlocal count          # without this, line below errors
        count += 1
        return count
    return step

c1 = make_counter()
c2 = make_counter()
print(c1())   # ?
print(c1())   # ?
print(c2())   # ?
print(c1())   # ?
```

Predicted? Run:

- `1` — first call to `c1` increments its own `count` from 0 to 1.
- `2` — second call: 1 → 2.
- `1` — `c2` has its own captured `count`. They don't share.
- `3` — `c1` keeps going independently.

`step` is a **closure** — a function that "closes over" a non-local
variable from its enclosing scope. Each call to `make_counter` creates
a fresh frame with a fresh `count`; the inner `step` keeps a
reference to that frame for its lifetime.

## Why `nonlocal`?

Without it, `count += 1` would treat `count` as a *new local* (because
of the assignment), and trying to read its old value before assignment
would error. `nonlocal count` says "I mean the `count` from the
enclosing function, not a fresh local." The analogous keyword for
module globals is `global`, but you'll use `nonlocal` more often in
day-to-day Python.

## The classic late-binding trap

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

[f() for f in funcs]    # [2, 2, 2]  (NOT [0, 1, 2])
```

Each lambda captured the *name* `i`, not its value at the time. By the
time we call them, `i` is 2. To capture by value, bind it as a
default:

```python
funcs = [lambda i=i: i for i in range(3)]   # [0, 1, 2]
```

Closures are powerful and easy to misuse. Day 27 leverages them to
build decorators.

## Now: open `02_fluency.py`

Three small scope/closure puzzles. Make each return what the test
expects.
