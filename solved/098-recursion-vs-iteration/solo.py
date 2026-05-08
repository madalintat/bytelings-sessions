"""Rung 4: Solo — solved version.

gcd uses the Euclidean algorithm: gcd(a, b) = gcd(b, a % b), base
  gcd(a, 0) = a. Recursion is natural here; the depth is O(log min(a,b)).

running_sum iterates, carrying a cumulative total.
"""


def gcd(a: int, b: int) -> int:
    """Greatest common divisor via Euclidean algorithm."""
    if b == 0:
        return a
    return gcd(b, a % b)


def running_sum(nums: list[int]) -> list[int]:
    """Return prefix sums: result[i] = sum(nums[0..i])."""
    result = []
    total = 0
    for x in nums:
        total += x
        result.append(total)
    return result
