"""Rung 2: Fluency drill — solved version.

Handle the ValueError for negative radius, then return pi * r^2.
Uses math.pi for correctness; pytest.approx in the tests handles
floating-point comparison.
"""
import math


def area_of_circle(radius: float) -> float:
    """Return pi * r^2. Raise ValueError if radius is negative."""
    if radius < 0:
        raise ValueError("negative radius")
    return math.pi * radius ** 2
