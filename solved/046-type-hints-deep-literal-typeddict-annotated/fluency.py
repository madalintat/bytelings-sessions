"""Rung 2: Fluency — solved version.

`TypedDict` gives a dict a typed schema that mypy/pyright can check.
`Literal["small", "medium", "large"]` narrows the `mode` parameter so
the type checker rejects any other string. Runtime behaviour is
unchanged.
"""
from typing import Literal, TypedDict


class User(TypedDict):
    id: int
    name: str


def describe(mode: Literal["small", "medium", "large"], user: User) -> str:
    return f"{user['name']} ({mode})"
