"""Rung 2: Fluency drill — answer four predict-the-output questions.

Topic: equality, identity, hashing
"""
from dataclasses import dataclass


@dataclass
class Mut:
    x: int


@dataclass(frozen=True)
class Imm:
    x: int


# Q1: are two Mut(1) instances equal (==)?
EQ_MUT = None  # TODO: True / False

# Q2: are two Mut(1) instances the same object (is)?
IS_MUT = None  # TODO: True / False

# Q3: is Imm hashable (can it be added to a set)?
HASHABLE_IMM = None  # TODO: True / False

# Q4: is Mut hashable (can it be added to a set)?
HASHABLE_MUT = None  # TODO: True / False
