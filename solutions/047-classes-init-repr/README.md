---
day: day-047-classes-init-repr
phase: phase-2-pythonic-tools
module: module-09-classes-dunders-context-managers
style: tour
---
# Day 47 — A code tour of a hand-written class

You've used dataclasses for a few days. Now we look under the hood.
Everything `@dataclass` did, you can do by hand. Sometimes you have to.

```python
class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

p = Point(3, 4)
print(p)                       # Point(x=3, y=4)
print(p.distance_from_origin())   # 5.0
```

## Line by line

`class Point:` — defines a new class, an object factory.

`def __init__(self, x, y):` — the **constructor**. When you call
`Point(3, 4)`, Python builds an empty object, then calls
`__init__` on it with `self` set to that new object plus the args you
passed. `self` isn't magic — it's just the conventional name for the
first parameter, which is the instance.

`self.x = x` — creates an attribute on the instance. After
`__init__`, the object carries `.x` and `.y`. There's no class-level
`x: int` declaration like in a dataclass; you bind the attribute by
assigning it.

`def __repr__(self) -> str:` — `repr(p)` and `print(p)` (when there's
no `__str__`) call this. The convention: return a string that *looks
like* a constructor call. This is the single best ROI of any dunder —
your debugger, your logs, your pytest failures all become readable.

`def distance_from_origin(self) -> float:` — a regular method.
First parameter is `self`. Call it as `p.distance_from_origin()` and
Python auto-passes `p` as `self`.

## `__init__` vs `__new__`

You'll see `__new__` in the wild. It runs *before* `__init__` and
actually creates the object. 99% of the time you don't override it —
override `__init__` instead. `__new__` matters when subclassing
immutable types (like `tuple` or `int`) where the value is fixed at
allocation time, not after.

## `__repr__` vs `__str__`

- `__repr__(self)` — the unambiguous developer-facing form. Aim for
  "if I pasted this into a REPL, I'd get an equal object back."
- `__str__(self)` — the user-facing form. Optional. Falls back to
  `__repr__` if you don't define it.

For most internal classes, just write a good `__repr__` and skip
`__str__`. Two people read your `repr`s daily for every one person
who sees a `str`: you, in the debugger, and you, six months from now.

## Why hand-write a class when dataclass exists?

- You have non-trivial `__init__` logic (validation, normalization).
- You're modeling behavior more than data — many methods, few fields.
- You're inheriting from a non-dataclass base.
- You want full control over the dunder set (Day 48–50 will add more).

For pure value bags, dataclass wins. For everything else, the
hand-written class is still the workhorse.

## Now: open `02_fluency.py`

A `Counter` class that's missing one method — guess which.
