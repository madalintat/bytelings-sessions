"""Rung 2: Fluency drill — fix the dataclass.

Topic: @dataclass + the mutable-default trap

`Cart` has the classic shared-list bug. Two carts end up sharing the
same `items` list. Fix the field declaration so each cart gets its own.
"""
from dataclasses import dataclass, field


@dataclass
class Cart:
    owner: str
    # TODO: this default is shared between all instances! Use field(default_factory=...)
    items: list[str] = None
