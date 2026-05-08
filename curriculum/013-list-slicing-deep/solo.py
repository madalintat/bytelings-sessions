"""Rung 4: Solo implement.

Topic: interleave two lists

Implement `interleave(a, b)`:

- Return a new list with elements alternating from `a` and `b`.
- Start with a[0], then b[0], then a[1], etc.
- If one list is longer, append its remaining tail at the end.
- Don't mutate the inputs.

Examples:
    interleave([1, 2, 3], ['a', 'b', 'c'])      -> [1, 'a', 2, 'b', 3, 'c']
    interleave([1, 2, 3, 4, 5], ['a', 'b'])     -> [1, 'a', 2, 'b', 3, 4, 5]
    interleave([], [1, 2])                       -> [1, 2]

Hint: list slicing makes the "tail" part trivial.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


def interleave(a: list, b: list) -> list:
    raise NotImplementedError
