"""Rung 2: Fluency — solved version.

smallest: heapq.heapify turns the list into a min-heap in place.
  The minimum is at index 0 (not -1 which is the last element).
  Change `h[-1]` to `h[0]`.

largest_three: `heapq.nsmallest` returns the k smallest values.
  We want the k LARGEST, so use `heapq.nlargest` instead.
  Both return results sorted in the appropriate order (nlargest
  returns descending, which matches the docstring's contract).
"""
import heapq


def smallest(values: list[int]) -> int:
    """Return the smallest of `values` using a heap. Raises IndexError if empty."""
    h = list(values)
    heapq.heapify(h)
    if not h:
        raise IndexError("smallest() called on empty sequence")
    return h[0]


def largest_three(values: list[int]) -> list[int]:
    """Return the three largest values, in descending order."""
    return heapq.nlargest(3, values)
