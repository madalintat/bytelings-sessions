"""Rung 3: Guided — solved version.

Clamp is `max(low, min(x, high))`. Read it inside-out:
  - min(x, high) bounds x from above (never bigger than high)
  - max(low, ...) bounds the result from below (never smaller than low)

Equivalent forms:
  if x < low: return low
  if x > high: return high
  return x

The nested-min-max form is one expression and reads as "the inner
boundary." Both are fine; pick whichever your codebase already uses.
"""


def clamp(x: float, low: float, high: float) -> float:
    """
    >>> clamp(5, 0, 10)
    5
    >>> clamp(-1, 0, 10)
    0
    >>> clamp(99, 0, 10)
    10
    """
    return max(low, min(x, high))
