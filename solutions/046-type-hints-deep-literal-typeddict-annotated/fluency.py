"""Rung 2: Fluency drill — tighten the types.

Topic: Literal + TypedDict

`describe(mode, user)` should:
1. Accept `mode` as a Literal of "small", "medium", or "large"
2. Accept `user` as a TypedDict with fields `id: int` and `name: str`

Define the TypedDict and use Literal in the signature. The runtime
behavior shouldn't change — the function still returns f"{name} ({mode})".
"""
from typing import Literal, TypedDict


# TODO: define a TypedDict User with id: int and name: str
class User(TypedDict):
    pass  # replace


# TODO: change `mode: str` to `mode: Literal["small", "medium", "large"]`
def describe(mode: str, user: User) -> str:
    return f"{user['name']} ({mode})"
