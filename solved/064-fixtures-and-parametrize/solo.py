"""Rung 4: Solo implement — solved version.

clamp(value, low, high): return low when value < low, high when value > high,
value otherwise. Raise ValueError when low > high. Uses only < comparisons
so it works on any type supporting them.
"""
from typing import TypeVar

T = TypeVar("T")


def clamp(value: T, low: T, high: T) -> T:
    if low > high:
        raise ValueError("low must be <= high")
    if value < low:
        return low
    if value > high:
        return high
    return value
