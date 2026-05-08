"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: an iterable that is NOT its own iterator

Build `Repeat(values, times)` — an *iterable* that, each time you
iterate it, yields `values` repeated `times` times.

Example:
    r = Repeat([1, 2], 3)
    list(r)   # [1, 2, 1, 2, 1, 2]
    list(r)   # [1, 2, 1, 2, 1, 2]   ← can re-iterate

Constraints:
- `Repeat` itself is iterable (has `__iter__`) but is NOT an iterator
  (does not implement `__next__`). Each `iter(repeat)` must return a
  *fresh* iterator object so the class supports multiple passes.
- `times == 0` yields nothing.
- `values` is any iterable (list, tuple, etc.).

Hint: define a small inner class for the iterator, or define a helper
class at module level.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


class Repeat:
    def __init__(self, values, times: int) -> None:
        raise NotImplementedError
