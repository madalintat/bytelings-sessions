"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: lazy infinite generator + take_while

Implement two generator functions:

1. `naturals()` — yields 1, 2, 3, 4, ... forever. No argument.

2. `take_while(predicate, source)` — yields items from `source` while
   `predicate(item)` is True. Stops at the first item where the
   predicate is False (and does NOT yield that item).

Constraints:
- `naturals` must be lazy. The function must use `yield`. Do NOT call
  `range(some_huge_number)`.
- `take_while` must be lazy too. It must stop pulling from `source` the
  moment the predicate fails.

Example:
    list(take_while(lambda n: n < 5, naturals()))   # [1, 2, 3, 4]

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.

Patterns: P-07 (accumulator-into-dict), P-12 (filter-then-map), P-16 (yield-from-passthrough), P-31 (string-build-via-list-then-join).
"""


def naturals():
    raise NotImplementedError


def take_while(predicate, source):
    raise NotImplementedError
