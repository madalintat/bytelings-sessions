"""Rung 4: Solo.

Topic: pick the right shape, then implement.

Implement two functions:

1. `gcd(a, b)` — the greatest common divisor of two positive ints.
   The classic Euclidean algorithm: gcd(a, b) = gcd(b, a % b).
   Base case: gcd(a, 0) = a. Use whichever shape you think fits;
   recursion is natural here because each step is a smaller problem.

2. `running_sum(nums)` — return a new list where the i-th item is
   the sum of nums[0..i]. Example: running_sum([3, 1, 4, 1, 5])
   returns [3, 4, 8, 9, 14]. Iteration fits this naturally.

Tests in 04_solo_test.py are HIDDEN.
"""


def gcd(a: int, b: int) -> int:
    raise NotImplementedError


def running_sum(nums: list[int]) -> list[int]:
    raise NotImplementedError
