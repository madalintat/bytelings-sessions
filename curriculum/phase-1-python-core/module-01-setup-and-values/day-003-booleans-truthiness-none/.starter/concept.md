---
day: day-003-booleans-truthiness-none
phase: phase-1-python-core
module: module-01-setup-and-values
style: compare
---
# Day 3 — `if x:` vs `if x is not None:`

Two snippets. Both look reasonable. Which one is right?

### Snippet A
```python
def show(name: str | None):
    if name:
        print(f"Hi, {name}")
    else:
        print("Hi, stranger")
```

### Snippet B
```python
def show(name: str | None):
    if name is not None:
        print(f"Hi, {name}")
    else:
        print("Hi, stranger")
```

Both compile. Both run. They behave **differently** when `name == ""`:

| Input | A says | B says |
|---|---|---|
| `"Bytelinger"` | "Hi, Bytelinger" | "Hi, Bytelinger" |
| `None` | "Hi, stranger" | "Hi, stranger" |
| `""` | "Hi, stranger" | "Hi, " |

Snippet A treats empty string the same as no name. Snippet B treats them
differently. Which is "right" depends on your intent.

## The rule

In Python, **truthiness** is built into a lot of types:
- `0`, `0.0`, `""`, `[]`, `{}`, `None` → falsy
- everything else → truthy

`if x:` checks truthiness. `if x is not None:` checks for None
specifically.

**When you mean "is this `None`?", say `is None`. When you mean
"does this have content?", use truthiness.** Mixing them up is one of
the most common Python bugs at code review time.

## And `is` vs `==`?

`is` checks identity (same object in memory). `==` checks equality.
For `None`, `True`, `False`: always use `is`. They're singletons.

```python
x = None
x == None       # works but lints flag it
x is None       # canonical
```

## Now: `02_fluency.py`

Three small predicate functions to fix.
