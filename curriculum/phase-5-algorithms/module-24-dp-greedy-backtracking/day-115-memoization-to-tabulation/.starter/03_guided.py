"""Rung 3: Guided — house robber, BOTH ways.

Topic: solve the same problem two ways.

You're a thief considering a row of houses, each with some non-
negative amount of money. You can't rob two adjacent houses
(silent alarms). What's the max money you can steal?

Implement BOTH:

`rob_topdown(houses)` — recursive with @cache.
`rob_bottomup(houses)` — iterative with a table or two rolling vars.

Both must return the same answer.

>>> rob_topdown([2, 7, 9, 3, 1])
12     # 2 + 9 + 1
>>> rob_bottomup([2, 7, 9, 3, 1])
12

Hints:
- Recurrence: best(i) = max(best(i-1), best(i-2) + houses[i])
- Base: best(-1) = 0, best(0) = houses[0].
- Top-down can take an index argument; bottom-up fills a table from
  index 0 up to len(houses) - 1.
"""
from functools import cache


def rob_topdown(houses: list[int]) -> int:
    raise NotImplementedError


def rob_bottomup(houses: list[int]) -> int:
    raise NotImplementedError
