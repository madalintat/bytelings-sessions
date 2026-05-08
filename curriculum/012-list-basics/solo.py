"""Rung 4: Solo implement.

Topic: rotate a list

Implement `rotate(items, k)`:

- Return a NEW list where each element has moved RIGHT by `k` positions
  (elements that fall off the right wrap around to the left).
- Negative `k` rotates left.
- `k` may be larger than len(items); take it mod len.
- Empty list returns [] for any k.
- Don't mutate the input.

Examples:
    rotate([1,2,3,4,5], 2)   -> [4,5,1,2,3]
    rotate([1,2,3,4,5], -1)  -> [2,3,4,5,1]
    rotate([1,2,3], 7)       -> [3,1,2]   (7 mod 3 == 1)

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


def rotate(items: list, k: int) -> list:
    raise NotImplementedError
