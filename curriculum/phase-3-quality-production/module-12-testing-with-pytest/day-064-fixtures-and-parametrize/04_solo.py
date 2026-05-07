"""Rung 4: Solo implement.

Topic: write the unit so a parametrized test passes.

Build `clamp(value, low, high)`:

  - Returns `value` if low <= value <= high.
  - Returns `low` if value < low.
  - Returns `high` if value > high.
  - Raises ValueError("low must be <= high") if low > high.
  - Works for ints, floats, and any types that support `<` (e.g., str).

Hidden tests in 04_solo_test.py — heavily parametrized.
"""
from typing import TypeVar

T = TypeVar("T")


def clamp(value: T, low: T, high: T) -> T:
    raise NotImplementedError
