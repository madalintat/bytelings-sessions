"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: a Protocol + a function that uses it

Define a Protocol called `Sized` that describes any object with a
`__len__` method returning int.

Then implement `longest(items)`:
- `items` is a list of objects each conforming to `Sized`.
- Return the item with the largest length.
- If `items` is empty, raise ValueError.
- Ties: return the first one encountered (stable behavior).

Type the function so the parameter is `list[Sized]` and the return
is `Sized`.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.

Patterns: P-15 (unpacking-into-named), P-21 (protocol-as-interface).
"""
from typing import Protocol


class Sized(Protocol):
    pass  # TODO: declare __len__(self) -> int with `...` body


def longest(items):
    raise NotImplementedError
