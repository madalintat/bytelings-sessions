"""Rung 2: Fluency — solved version.

parent_index: the correct formula is (i - 1) // 2. The stub uses
  i // 2, which is off for all odd indices: parent(1) should be 0
  but i//2 gives 0 — that one accidentally passes. For i=3,
  (3-1)//2 = 1 (correct) vs 3//2 = 1 (accidentally right), but
  for i=2, (2-1)//2 = 0 (correct) vs 2//2 = 1 (wrong). Fix:
  subtract 1 before dividing.

smaller_child_index: the stub always returns `left`, ignoring whether
  `right` is smaller. Fix by checking if `right < n` and if
  data[right] < data[left]; if so, return right.
"""


def parent_index(i: int) -> int:
    """Return the parent index of `i` in a 0-indexed binary heap."""
    if i == 0:
        return 0
    return (i - 1) // 2


def smaller_child_index(data: list, i: int) -> int:
    """Return the index of the smaller child of `i`, or -1 if none."""
    n = len(data)
    left = 2 * i + 1
    right = 2 * i + 2
    if left >= n:
        return -1
    if right < n and data[right] < data[left]:
        return right
    return left
