"""Rung 3: Guided — solved version.

Both lower_bound and upper_bound use the "always narrow toward the
answer" template: lo = 0, hi = len(arr) (not len - 1), loop while
lo < hi, and never return early on a match. At the end lo == hi and
that index is the answer.

lower_bound narrows by:
  arr[mid] < target  →  lo = mid + 1   (mid is too small)
  else               →  hi = mid       (mid might be the answer)

upper_bound narrows by:
  arr[mid] <= target →  lo = mid + 1   (mid is not strictly larger)
  else               →  hi = mid
"""


def lower_bound(arr: list[int], target: int) -> int:
    """Index of first element >= target. len(arr) if all elements < target."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(arr: list[int], target: int) -> int:
    """Index of first element > target. len(arr) if all elements <= target."""
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo
