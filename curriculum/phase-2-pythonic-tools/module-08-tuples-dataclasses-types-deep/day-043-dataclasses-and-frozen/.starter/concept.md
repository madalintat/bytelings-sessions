---
day: day-043-dataclasses-and-frozen
phase: phase-2-pythonic-tools
module: module-08-tuples-dataclasses-types-deep
style: tour
---
# Day 43 — A code tour of `@dataclass`

Read this whole snippet. Then we'll walk it.

```python
from dataclasses import dataclass, field

@dataclass
class User:
    id: int
    name: str
    email: str = ""
    tags: list[str] = field(default_factory=list)

u = User(id=1, name="Mada")
print(u)             # User(id=1, name='Mada', email='', tags=[])
print(u == User(id=1, name="Mada"))   # True
u.tags.append("admin")
print(u.tags)        # ['admin']
```

## Line by line

`@dataclass` — a class decorator from the standard library. It reads
the typed attributes you wrote and synthesizes the boring methods for
you: `__init__`, `__repr__`, `__eq__`. No more 12-line `__init__` that
just assigns `self.x = x` six times.

`id: int` and `name: str` — these are class-level type annotations.
With `@dataclass`, they become **fields** of the generated `__init__`
in declaration order.

`email: str = ""` — a field with a default. Like normal function args,
fields with defaults must come after fields without.

`tags: list[str] = field(default_factory=list)` — the *one* non-obvious
rule. You can't write `tags: list = []`. Why? Because that one list
would be shared across every instance — the classic mutable-default
bug. `field(default_factory=list)` says "call `list()` for each new
instance," giving everyone their own.

`u = User(id=1, name="Mada")` — the synthesized `__init__` accepts
fields by position or by keyword.

`print(u)` — the synthesized `__repr__` is the constructor call you
would have written. Hugely useful in logs and tests.

`u == User(id=1, name="Mada")` — the synthesized `__eq__` compares
field-by-field. Two dataclasses are equal if every field is equal.

## `frozen=True`: when mutation is a bug, not a feature

```python
@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
p.x = 99       # raises FrozenInstanceError
```

Frozen dataclasses can't be mutated after construction. They're also
**hashable**, which means you can use them as dict keys or set members.
This is your default for "value objects" — things like `Point`,
`Money`, `Email`, `Coordinate`. Mutability would be a bug there
anyway.

Mutable dataclasses (the default) are NOT hashable. If you need both
mutability and hashability, the answer is "you don't" — pick one.

## Dataclass vs NamedTuple — when to pick which

A NamedTuple *is* a tuple — you can index it, unpack it, iterate it.
A dataclass is a regular class. Pick a NamedTuple when the
"this is a record" framing matters and tuple ergonomics help. Pick
`@dataclass` (especially `frozen=True`) when you want the value
without the tuple-ness; or when you have many fields, mutable state,
or want methods on the class.

## A few more options worth knowing

- `@dataclass(slots=True)` — generates `__slots__`. Less memory, no
  `__dict__`. Use it for tiny value objects you make many of.
- `@dataclass(order=True)` — generates `<`, `<=`, `>`, `>=` field-by-field.
- `field(init=False, default=...)` — a field that's NOT in `__init__`
  (set in `__post_init__`).

## Now: open `02_fluency.py`

A dataclass with the mutable-default bug. Fix it.
