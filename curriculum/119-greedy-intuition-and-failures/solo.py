"""Rung 4: Solo.

Topic: minimum number of railway platforms.

Given two sorted arrays `arrivals` and `departures` of the same length,
return the minimum number of platforms needed at a railway station so
that no train has to wait on the track.

Two trains can share a platform if one departs before the next arrives.

>>> min_platforms([900, 940, 950, 1100, 1500, 1800],
...               [910, 1200, 1120, 1130, 1900, 2000])
3

Greedy approach:
- Sort both arrays (they may not be sorted when passed in).
- Use two pointers i (arrivals) and j (departures).
- When the next event is an arrival (arr[i] < dep[j]), a new platform is
  needed: platforms_needed += 1. Advance i.
- When the next event is a departure (arr[i] >= dep[j]), a platform is
  freed: platforms_needed -= 1. Advance j.
- Track the maximum platforms_needed seen at any point.
- O(n log n) for the sorts, O(n) scan.

Tests in solo_test.py are HIDDEN.

Hints:
- Sort both arrays first even if the docstring examples look sorted.
- The loop runs while i < len(arrivals) (all arrivals must be processed).
- A train departing at time T frees the platform; another arriving at T
  needs a new one — treat arrival first (use strict <).
"""


def min_platforms(arrivals: list[int], departures: list[int]) -> int:
    raise NotImplementedError
