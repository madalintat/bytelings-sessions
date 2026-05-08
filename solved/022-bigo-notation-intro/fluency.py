"""Rung 2: Fluency — solved version.

Fill in the Big-O constants. The functions themselves already work.

  BIGO_FIRST_ITEM = "O(1)"    — array index is constant time.
  BIGO_SUM_ITEMS  = "O(n)"    — one pass through all items.
  BIGO_HAS_PAIR_NAIVE = "O(n^2)" — nested loop: O(n * (n-1)/2) ≈ O(n^2).
  BIGO_SORT = "O(n log n)"    — Python's Timsort is O(n log n) worst case.

The notation "O(n log n)" uses a space (not "*") per the test contract.
"""

BIGO_FIRST_ITEM = "O(1)"
BIGO_SUM_ITEMS = "O(n)"
BIGO_HAS_PAIR_NAIVE = "O(n^2)"
BIGO_SORT = "O(n log n)"


def first_item(items: list):
    """Return the first item."""
    return items[0]


def sum_items(items: list[int]) -> int:
    """Return the sum of items."""
    total = 0
    for x in items:
        total += x
    return total


def has_pair_naive(items: list[int], target: int) -> bool:
    """Return True if any two distinct items sum to `target`."""
    n = len(items)
    for i in range(n):
        for j in range(i + 1, n):
            if items[i] + items[j] == target:
                return True
    return False


def my_sort(items: list) -> list:
    """Return a sorted copy."""
    return sorted(items)
