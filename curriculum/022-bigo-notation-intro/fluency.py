"""Rung 2: Fluency drill — name the Big-O.

Topic: classifying small algorithms

Each function below already works. Your job is to fill in the
constants `BIGO_*` to declare the Big-O shape of the worst case.

Use one of these strings exactly:
  "O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)"
"""

# TODO: pick the right shape for each function below

BIGO_FIRST_ITEM = "O(?)"
BIGO_SUM_ITEMS = "O(?)"
BIGO_HAS_PAIR_NAIVE = "O(?)"
BIGO_SORT = "O(?)"


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
