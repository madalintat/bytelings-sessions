---
day: 048-properties-eq-hash
phase: phase-2-pythonic-tools
module: module-09-classes-dunders-context-managers
style: detective
---
# Day 48 — The case of the disappearing user

A teammate is debugging a flaky cache. They paste this code:

```python
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id

cache = {}
u = User(1, "Bytelinger")
cache[u] = "first time"
print(cache[User(1, "Bytelinger")])
```

It crashes with `KeyError: User(...)`. They swear `__eq__` is right —
two users with id=1 should be equal. But the dict can't find the key.

What's going on?

## Suspect 1: hashable-equal contract

When you override `__eq__`, Python *removes* the default `__hash__`.
Mutable user-defined classes with custom `__eq__` end up with
`__hash__ = None`, which means the class is no longer hashable. But
in fact, both `User` instances above ARE still hashable (Python only
removes `__hash__` if `__eq__` is overridden — but here `__hash__`
hasn't been removed in the way you'd expect).

Wait — that's not the bug. Let's check carefully.

In CPython, defining `__eq__` automatically sets `__hash__ = None`,
making instances unhashable. So `cache[u] = ...` should have already
raised `TypeError`. Unless... Python *only* does this when `__eq__` is
defined in a class that doesn't define `__hash__`.

Try the code in a REPL: `cache[u]` succeeds at write-time but fails on
lookup. Why? Because `__hash__` *was* still inherited from `object` —
the default hash is based on `id(self)`. The two `User(1, "Bytelinger")`
instances are different objects, so they hash to different buckets.
Equal but unequal hashes. Lookup fails.

This is the contract: **if a == b, then hash(a) must equal hash(b)**.
Otherwise dicts and sets break.

## The fix: override `__hash__` to match

```python
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id
    def __hash__(self):
        return hash(self.id)
```

Now both instances hash to `hash(1)` and the dict finds the key.

A simpler fix when you can: use `@dataclass(frozen=True)`. It generates
`__eq__` and `__hash__` together, correctly.

## `@property`: the other half of today

Sometimes you want an attribute that's *computed* — like `User.full_name`
from `first` and `last`. Without help, you'd have to call `u.full_name()`.
With `@property`, you write a method but call it as an attribute:

```python
class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property
    def full_name(self) -> str:
        return f"{self.first} {self.last}"

u = User("M", "T")
u.full_name        # "M T"   — no parens!
```

Properties are also how you make attributes *read-only* or *validated
on set*: define a setter (`@full_name.setter`) that does the check.

The pattern: **start with a plain attribute. Switch to `@property`
when you need computation, validation, or read-only access** — without
breaking the existing `obj.x` usage sites.

## Now: open `fluency.py`

A class that overrides `__eq__` but forgot `__hash__`. Convict it.
