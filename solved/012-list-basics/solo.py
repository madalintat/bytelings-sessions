"""Rung 4: Solo — solved version.

`rotate` right by k: slice the list at position `n - k` (mod n) and
swap the two halves.

For a list of length n, rotating right by k means:
  result = items[-(k % n):] + items[:-(k % n)]

The `k % n` handles k larger than len(items) and negative k in one shot,
because Python's modulo for negative numbers follows the sign of the divisor.
For example, k=-1 with n=5 gives -1 % 5 = 4, which rotates right by 4 =
rotates left by 1, as expected.

Edge case: n == 0 is handled by the early return. When k % n == 0,
both slice and concatenation produce a copy of the original.
"""


def rotate(items: list, k: int) -> list:
    if not items:
        return []
    n = len(items)
    k = k % n
    return items[-k:] + items[:-k] if k else list(items)
