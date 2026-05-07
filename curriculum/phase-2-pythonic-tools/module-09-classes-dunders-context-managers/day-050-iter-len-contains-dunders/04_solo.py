"""Rung 4: Solo implement. No scaffold beyond the spec.

Topic: a small ordered set that speaks the container protocol

Build `OrderedSet` — a collection that:
- Preserves insertion order.
- Doesn't add an item that's already present.
- Supports len(), iteration, and `x in s` (the last must be O(1) on
  average — back it with a dict or set under the hood).

API:
- __init__(self, items=None): items is an optional iterable.
- add(self, item) -> None
- __len__, __iter__, __contains__
- __repr__ returns f"OrderedSet({list(self)!r})"

Constraints:
- Items must be hashable.
- The `in` check must NOT iterate through the items linearly — back it
  with a dict or set (the test will check via a large input).

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


class OrderedSet:
    def __init__(self, items=None) -> None:
        raise NotImplementedError
