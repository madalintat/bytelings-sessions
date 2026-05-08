"""Rung 4: Solo — solved version.

`running_diffs` computes consecutive differences using the
`zip(items, items[1:])` pattern:

  - `items[1:]` is a slice that starts from the second element.
  - `zip(items, items[1:])` pairs each element with its successor.
  - A list comprehension computes `b - a` for each pair.

This produces a list of length `n - 1` without any explicit index
management. Empty and single-item lists naturally yield [] because
`zip` returns 0 pairs in those cases.
"""


def running_diffs(items: list[float]) -> list[float]:
    return [b - a for a, b in zip(items, items[1:])]
