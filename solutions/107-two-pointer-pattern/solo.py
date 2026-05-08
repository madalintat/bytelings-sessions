"""Rung 4: Solo.

Topic: remove duplicates in place using fast/slow two-pointer.

Given a SORTED list with duplicates, modify it in place so the first
k positions contain each unique value once (in original order), and
return k.

The contents of arr after position k don't matter (the test only
checks arr[:k]).

>>> arr = [1, 1, 2, 3, 3, 3, 4]
>>> k = remove_duplicates(arr)
>>> k
4
>>> arr[:k]
[1, 2, 3, 4]

Hints:
- slow = 0 (last unique). fast = 1 (scanner).
- Walk fast forward. When arr[fast] != arr[slow], it's a new value:
  slow += 1, write arr[slow] = arr[fast].
- Return slow + 1 at the end (size of unique prefix).

Tests in 04_solo_test.py are HIDDEN.

Patterns: P-08 (two-pointer-from-ends), P-09 (two-pointer-fast-slow).
"""


def remove_duplicates(arr: list[int]) -> int:
    raise NotImplementedError
