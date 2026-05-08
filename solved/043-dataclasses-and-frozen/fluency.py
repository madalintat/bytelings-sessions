"""Rung 2: Fluency — solved version.

The classic mutable-default trap: `items: list[str] = []` stores one
list object and every `Cart` instance would share it. `field(default_factory=list)`
tells the dataclass machinery to call `list()` fresh for every new
instance, giving each cart its own independent list.
"""
from dataclasses import dataclass, field


@dataclass
class Cart:
    owner: str
    items: list[str] = field(default_factory=list)
