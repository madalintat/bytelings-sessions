"""Rung 2: Fluency — solved version.

Mut is a plain dataclass (not frozen): its `__eq__` compares by field
values (so two `Mut(1)` are equal) but they are *different objects*
(not identical). Because Mut is not frozen, Python sets `__hash__ = None`
(mutable dataclasses are unhashable by default). Imm is frozen, so it
is both equated by value and hashable.
"""
from dataclasses import dataclass


@dataclass
class Mut:
    x: int


@dataclass(frozen=True)
class Imm:
    x: int


EQ_MUT = True       # two Mut(1) compare equal via dataclass __eq__
IS_MUT = False      # two Mut(1) are distinct objects
HASHABLE_IMM = True   # frozen dataclass gets __hash__
HASHABLE_MUT = False  # non-frozen dataclass sets __hash__ = None
