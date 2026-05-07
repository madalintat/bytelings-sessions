"""Rung 4: Solo implement.

Topic: write a function whose CORRECTNESS is described by properties.

Implement `merge_sorted(a, b) -> list`:

  - `a` and `b` are each sorted ascending lists of ints.
  - Return a single sorted ascending list containing all items from
    both (with duplicates preserved — it's a multiset merge).

Properties the hidden tests check:
  - len(merge_sorted(a,b)) == len(a) + len(b)
  - the result is sorted
  - sorted(merge_sorted(a,b)) == sorted(a + b)  (multiset equality)
  - merge_sorted(a, []) == a; merge_sorted([], b) == b

Hint: classic two-pointer merge is O(n+m). A naive `sorted(a+b)` will
also pass these tests but is O((n+m) log (n+m)) — try the two-pointer
version for the practice.
"""


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    raise NotImplementedError
