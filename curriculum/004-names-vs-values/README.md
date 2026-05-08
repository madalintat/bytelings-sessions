---
day: day-004-names-vs-values
phase: phase-1-python-core
module: module-01-setup-and-values
style: trace
---
# Day 4 — Trace this: when does the list change?

You see this code. Predict each `print` *before* you run it.

```python
def append_to(lst, x):
    lst.append(x)

a = [1, 2, 3]
b = a
append_to(a, 4)
print(a)        # ?
print(b)        # ?
print(a is b)   # ?

c = a + [5]
print(c)        # ?
print(a)        # ?
print(a is c)   # ?
```

Did you guess?

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
True
[1, 2, 3, 4, 5]
[1, 2, 3, 4]
False
```

The trick: `a` and `b` are two **names** for the **same list**. They
point at the same object in memory. Mutating through one shows in
the other. That's why `b` "magically" updated when you only touched `a`.

But `a + [5]` creates a *new* list — addition doesn't mutate `a`. So
`c` is a different object. `a is c` is False.

## The mental model

- **Variables in Python are names, not boxes.** `b = a` does NOT
  copy. It binds another name to the same object.
- **`is` checks identity** (same object in memory).
- **`==` checks equality** (same value, possibly different object).
- **Mutation visible everywhere** that name points; rebinding (`a = ...`)
  only affects that name.

This is the source of 80% of "but I didn't change that variable" bugs.

## Now: trace through `fluency.py`

You'll fix a function so it doesn't silently mutate its caller's list.
