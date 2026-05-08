"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: a streaming pipeline of generator expressions

Implement `top_n_lengths(strings, n)` that returns the lengths of the
`n` longest strings, sorted descending, ties broken by earlier-first.

Constraints:
- `strings` may be any iterable (including a generator).
- You must NOT call `list(strings)` or otherwise materialize the whole
  iterable before processing. Use generator expressions to produce
  (length, index) pairs and sort those.
- If n <= 0 return [].

Hint: `sorted(...)` returns a list, but it accepts any iterable. You
can sort a generator expression directly.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


def top_n_lengths(strings, n: int) -> list[int]:
    raise NotImplementedError
