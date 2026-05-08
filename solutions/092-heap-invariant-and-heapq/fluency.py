"""Rung 2: Fluency drill — fix two heapq idioms.

Topic: heapq is min-only; using a tuple key for priority.
"""
import heapq


def smallest(values: list[int]) -> int:
    """Return the smallest of `values` using a heap. Raises IndexError if empty.

    The cheap idiom: heapify in place (O(n)) and read index 0.
    """
    # TODO: this returns the LAST element instead of the smallest.
    h = list(values)
    heapq.heapify(h)
    return h[-1]


def largest_three(values: list[int]) -> list[int]:
    """Return the three largest values, in descending order.

    For example: largest_three([5, 1, 9, 3, 7, 2]) -> [9, 7, 5].

    If there are fewer than 3 values, return all of them in descending order.

    Hint: heapq.nlargest exists and does exactly this.
    """
    # TODO: nsmallest gives the smallest. Use the right helper.
    return heapq.nsmallest(3, values)
