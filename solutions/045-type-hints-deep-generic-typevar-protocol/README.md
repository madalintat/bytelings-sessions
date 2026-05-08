---
day: day-045-type-hints-deep-generic-typevar-protocol
phase: phase-2-pythonic-tools
module: module-08-tuples-dataclasses-types-deep
style: build-it
---
# Day 45 — Pretend Python doesn't have generics. Build them.

Surface type hints (Day 5) are easy. The deep ones — generics, TypeVars,
Protocols — feel mysterious until you see what they're solving. So
let's build the same idea by hand first.

## The problem: a typed stack

You want a `Stack` class. It can hold anything. But you want type
checkers to know that if you put `int`s in, you get `int`s out.

Without generics, you'd have to write `IntStack`, `StrStack`, `UserStack`
— a class per element type. Or you'd type everything as `object` and
lose all useful checking. Both are bad.

## The fix: TypeVar

A **TypeVar** is a placeholder. "I don't care what type, but it's the
same type throughout this thing."

```python
from typing import TypeVar, Generic

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()
```

`Generic[T]` declares the class is parameterized by `T`. Now usage:

```python
s: Stack[int] = Stack()
s.push(7)
s.push("oops")        # type checker: error — expected int
n: int = s.pop()      # type checker: this is int
```

At runtime, none of this is enforced — Python doesn't actually check.
The point is the *type checker* (mypy, Pyright) catches mismatches
before code runs.

## Functions can be generic too

```python
def first(items: list[T]) -> T:
    return items[0]

x = first([1, 2, 3])      # x: int
y = first(["a", "b"])     # y: str
```

The same `T` appears on both sides — input and output share a type.

## Protocols: structural typing

A `Protocol` says "any class with these methods, regardless of
inheritance." It's duck typing with a type-checker-friendly contract.

```python
from typing import Protocol

class HasLen(Protocol):
    def __len__(self) -> int: ...

def is_empty(x: HasLen) -> bool:
    return len(x) == 0

is_empty([])      # ok — list has __len__
is_empty("")      # ok — str has __len__
is_empty({"a": 1})  # ok — dict has __len__
```

No class had to inherit from `HasLen`. The type checker sees that they
all implement the structural shape and waves them through.

This is huge in real code: you can declare "I take any object that
quacks like a duck" without forcing every duck to inherit from a
common base class.

## Generic + Protocol together

You can combine them. A `Sortable` protocol parameterized by `T`,
a `sort` function generic over `T`. The type system gets richer as
you stack pieces, but the building blocks are these three: `TypeVar`,
`Generic[T]`, `Protocol`.

## Now: open `fluency.py`

A `Box` class that's missing its TypeVar and Generic declaration.
