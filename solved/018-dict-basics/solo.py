"""Rung 4: Solo — solved version.

`invert` builds a new dict with keys and values swapped. When multiple
keys map to the same value, the LAST one wins because each assignment
overwrites the previous entry for that key.

A dict comprehension `{v: k for k, v in d.items()}` is the idiomatic
one-liner. Python dicts preserve insertion order (3.7+), so the last
assignment for a given value key survives.

The test verifies the input is not mutated and the result is a new dict.
"""


def invert(d: dict) -> dict:
    return {v: k for k, v in d.items()}
