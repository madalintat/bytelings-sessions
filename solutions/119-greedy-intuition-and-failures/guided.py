"""Rung 3: Guided — activity selection by finish time.

Topic: classic greedy — sort by earliest finish, scan greedily.

`select_activities` receives a list of (start, finish) tuples and
returns the maximum-size subset of non-overlapping activities.

Ties in finish time can be broken arbitrarily.

>>> select_activities([(1, 4), (3, 5), (0, 6), (5, 7)])
[(1, 4), (5, 7)]

Algorithm:
  1. Sort by finish time.
  2. Keep a `last_finish` cursor (start at −∞).
  3. For each activity in sorted order, take it if start >= last_finish;
     update last_finish to its finish.

Return the chosen list in finish-time order.

Hints:
- sorted(activities, key=lambda a: a[1])
- An activity is compatible if start >= last_finish (not strict >):
  back-to-back activities are allowed.
"""


def select_activities(activities: list[tuple[int, int]]) -> list[tuple[int, int]]:
    raise NotImplementedError
