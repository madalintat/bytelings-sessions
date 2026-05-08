---
day: 044-equality-identity-hashing-semantics
phase: phase-2-pythonic-tools
module: module-08-tuples-dataclasses-types-deep
style: trace
---
# Day 44 — Trace this: equal, identical, or hashable?

Predict every line *before* you run it.

```python
from dataclasses import dataclass

@dataclass
class A:
    x: int

@dataclass(frozen=True)
class B:
    x: int

a1 = A(1); a2 = A(1)
b1 = B(1); b2 = B(1)

print(a1 == a2)        # ?
print(a1 is a2)        # ?
print(b1 == b2)        # ?
print(b1 is b2)        # ?

s = set()
s.add(b1); s.add(b2)
print(len(s))          # ?
try:
    set([a1])
    print("A is hashable")
except TypeError:
    print("A is NOT hashable")
```

Output:

```text
True
False
True
False
1
A is NOT hashable
```

Walk through it:

`a1 == a2` → True. Dataclass `__eq__` compares fields. Both have x=1.

`a1 is a2` → False. Two separate constructor calls produce two
distinct objects.

`b1 == b2` → True, same reason as above (frozen doesn't change equality).

`b1 is b2` → False. Same reason — different constructions.

`len(s) == 1` → adding `b1` and `b2` to a set, but they hash equal and
compare equal, so the set keeps one. Frozen dataclasses are hashable.

`set([a1])` → TypeError. Plain `@dataclass` is mutable, and Python
disables hashing on mutable classes whose `__eq__` was overridden. The
fix is `frozen=True` (or `eq=False`).

## The three relations

- **Identity (`is`)** — same object in memory. `id(x) == id(y)`.
- **Equality (`==`)** — same value, by whatever rule `__eq__` defines.
  Default `__eq__` (object's) is identity, so for plain classes
  `a == b` is the same as `a is b` until you override.
- **Hashable** — has a `__hash__` that's consistent with `__eq__`.
  Required for dict keys and set members.

The contract: **equal objects must hash equal**. If you override `__eq__`
without overriding `__hash__`, Python *removes* `__hash__` so you don't
accidentally violate the contract.

## Why mutability and hashing don't mix

Dicts and sets place an object in a bucket by its hash. If the object
mutates after insertion such that its hash changes, lookups silently
fail — the object is "in" the dict but not at the bucket the lookup
checks. Python's solution: mutable types are non-hashable.

That's why `list` is unhashable but `tuple` is hashable.
That's why `dict` is unhashable but `frozenset` is hashable.
That's why `@dataclass` is unhashable but `@dataclass(frozen=True)` is
hashable.

## The cheat sheet

| Class kind | Equal by value? | Hashable? |
|---|---|---|
| Plain class (no overrides) | No (identity) | Yes (by id) |
| `@dataclass` | Yes | No |
| `@dataclass(frozen=True)` | Yes | Yes |
| `NamedTuple` subclass | Yes | Yes |

## Now: open `fluency.py`

Two tiny predict-the-output assertions about the rules above.
