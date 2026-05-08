"""Rung 2: Fluency — solved version.

forward: to produce [1, 2, ..., n] the recursive call must happen
  FIRST (building the rest of the list) and then n is appended at the
  END. The stub puts [n] before rest; swapping gives rest + [n] which
  builds ascending.

backward: to produce [n, n-1, ..., 1] the current value n must come
  FIRST, then the recursive result. The stub puts rest before [n];
  swapping gives [n] + rest which builds descending.
"""


def forward(n: int) -> list[int]:
    """Return [1, 2, ..., n]. Counts UP."""
    if n == 0:
        return []
    rest = forward(n - 1)
    return rest + [n]


def backward(n: int) -> list[int]:
    """Return [n, n-1, ..., 1]. Counts DOWN."""
    if n == 0:
        return []
    rest = backward(n - 1)
    return [n] + rest
