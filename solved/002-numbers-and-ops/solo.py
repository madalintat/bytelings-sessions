"""Rung 4: Solo — solved version.

Two idiomatic shapes; pick whichever you find clearer.

  Shape A — convert to string, sum the digit chars:
      sum(int(c) for c in str(n))
  Shape B — peel digits with divmod, accumulate:
      total = 0
      while n:
          n, d = divmod(n, 10)
          total += d
      return total

Shape A is shorter and reads as "what we mean." Shape B avoids the
str→int round-trip and is what you'd write in a language without
that convenience. Pick A unless you're being asked about
performance.

The base case (n == 0) is handled correctly by both: Shape A's
str(0) is "0" → sum is 0; Shape B's `while n` loop doesn't enter,
returning the initial 0.
"""


def digit_sum(n: int) -> int:
    return sum(int(c) for c in str(n))
