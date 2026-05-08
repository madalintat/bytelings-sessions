---
day: day-024-args-kwargs-defaults
phase: phase-1-python-core
module: module-05-functions-closures-decorators
style: detective
---
# Day 24 — The bug that won't reproduce

A teammate writes a function that "appends an item to a list." She
runs the unit test on Monday: green. She ships it. By Wednesday, a
bug report:

> "The history shows EVERYBODY's items, not just mine."

You ask for the function. She shows you:

```python
def add_to_history(item, history=[]):
    history.append(item)
    return history
```

You call it twice with no `history` argument:

```python
>>> add_to_history("a")
['a']
>>> add_to_history("b")
['a', 'b']        # ← bug
```

Two callers. Two histories. The list is shared.

## Why

**Default arguments are evaluated once, at function-definition time,
and stored on the function object.** That `[]` is a single list,
re-bound to the parameter `history` every time the function is called
without a value. Mutating it mutates the *one* list, forever.

You can see it:

```python
add_to_history.__defaults__   # ([],)   — the SAME list each call
```

## The fix

Use `None` as a sentinel and create the real default inside:

```python
def add_to_history(item, history=None):
    if history is None:
        history = []
    history.append(item)
    return history
```

Now each call without `history` gets its own fresh list.

The rule: **never use mutable defaults** (`list`, `dict`, `set`,
custom mutable objects). Immutable defaults (`int`, `str`, `tuple`,
`None`) are safe — there's nothing to mutate.

## While we're at it: `*args` and `**kwargs`

You'll see these on every wrapper, every decorator, every "pass it
through" function. Read them as:

- **`*args`** — collects extra POSITIONAL arguments into a tuple.
- **`**kwargs`** — collects extra KEYWORD arguments into a dict.

```python
def log_call(name, *args, **kwargs):
    print(f"calling {name} with {args} and {kwargs}")

log_call("fn", 1, 2, x=3, y=4)
# calling fn with (1, 2) and {'x': 3, 'y': 4}
```

The `*` and `**` work as **unpacking** at the call site too:

```python
nums = [1, 2, 3]
opts = {"sep": ", ", "end": "!\n"}
print(*nums, **opts)
# 1, 2, 3!
```

## Putting it all together: a full signature

```python
def fn(pos1, pos2, /, normal, *args, kw_only, **kwargs):
    ...
```

Reading left to right:

- `pos1, pos2, /` — positional-only (rare; covered later).
- `normal` — positional or keyword.
- `*args` — extra positionals.
- `kw_only` — must be passed by keyword.
- `**kwargs` — extra keyword args.

You'll write `def f(*, ..., **kwargs):` more often than the full
form. The bare `*` means "everything to my right is keyword-only" —
the same trick from Day 23.

## Now: open `02_fluency.py`

Detective work: each function has a default-arg or unpacking bug.
Patch each.
