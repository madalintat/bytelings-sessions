"""Rung 4: Solo — solved version.

`interleave` zips the two lists to get the paired portion, then appends
the tail of whichever list is longer.

The zip-based approach:
  - `zip(a, b)` stops at the shorter list.
  - Flatten each (x, y) pair into the result.
  - Append `a[len(b):]` or `b[len(a):]` for the remaining tail.

Using `min_len = min(len(a), len(b))` makes the slicing explicit.
The result is built with a list comprehension + concatenation, all O(n).

Alternative using itertools.chain and itertools.zip_longest, but the
plain slice approach is clearer for this exercise.
"""


def interleave(a: list, b: list) -> list:
    min_len = min(len(a), len(b))
    result = []
    for x, y in zip(a, b):
        result.append(x)
        result.append(y)
    result.extend(a[min_len:])
    result.extend(b[min_len:])
    return result
