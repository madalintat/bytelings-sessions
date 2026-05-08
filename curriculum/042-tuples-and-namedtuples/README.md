---
day: 042-tuples-and-namedtuples
phase: phase-2-pythonic-tools
module: module-08-tuples-dataclasses-types-deep
style: compare
---
# Day 42 — `point = (3, 4)` vs `Point(x=3, y=4)`

You see two ways to model a 2D point in code. Read both, then guess which
one ages well.

```python
# A — plain tuple
point = (3, 4)
distance = (point[0] ** 2 + point[1] ** 2) ** 0.5
```

```python
# B — namedtuple
from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int

point = Point(3, 4)
distance = (point.x ** 2 + point.y ** 2) ** 0.5
```

Same data, same memory cost (a `NamedTuple` *is* a tuple under the
hood). Same immutability. The difference is who has to remember what
each slot means.

In snippet A, six months from now, you'll see `point[0]` and need to
read upstream to figure out whether 0 is x, lat, hour, or width. In
snippet B, `point.x` says exactly what it is.

## When a plain tuple is fine

- A short, throwaway return: `return key, value`.
- An anonymous record in a hot inner loop where the names would just
  be noise.
- Function arguments where the position is universal: `(width, height)`.

A tuple gives you immutability, hashability (so it can be a dict key
or set member), and zero ceremony.

## When `NamedTuple` earns its keep

- The shape will be passed around or returned from functions.
- More than ~3 fields, or non-obvious order.
- You want type hints on the fields.
- You want `repr` for free: `Point(x=3, y=4)` instead of `(3, 4)`.

A `NamedTuple` is *still a tuple*. It iterates, unpacks, indexes, and
compares like a tuple:

```python
p = Point(3, 4)
x, y = p              # unpacks
p[0] == p.x           # True
list(p) == [3, 4]     # True
```

So you keep all the tuple ergonomics and add named access.

## And `collections.namedtuple` (older form)

```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
```

Works the same, but no type hints in the definition. Modern code uses
`typing.NamedTuple` for the typed declaration. Treat
`collections.namedtuple` as the older sibling — fine when you see it,
not what you reach for first.

## Tuples are immutable, but their contents may not be

```python
weird = (1, 2, [3, 4])
weird[2].append(5)        # WORKS — the list inside is mutable
weird[2] = [9]            # FAILS — can't reassign tuple slot
```

The tuple itself can't change which objects it points at. The objects
themselves are still whatever they are. Same gotcha as Day 4's
`a is b`.

## Now: open `fluency.py`

A function returns a plain tuple where a `NamedTuple` would clarify it.
