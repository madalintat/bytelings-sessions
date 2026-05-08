"""Rung 4: Solo implement.

Topic: bag-of-letters comparison

Implement `letter_diff(a, b)`:

- Both args are strings. Compare them letter-by-letter as MULTISETS
  (case-sensitive; whitespace and punctuation count as characters too).
- Return a dict {char: count} of characters that differ:
  - If `a` has more of char x than `b` has, count is positive
    (count = a_count - b_count).
  - If `b` has more of char x than `a` has, count is negative.
  - Characters that appear the same number of times in both are NOT
    in the result.
- Empty difference -> empty dict.

Examples:
    letter_diff("aabc", "abc")    -> {'a': 1}
    letter_diff("hello", "world") -> {'h': 1, 'e': 1, 'l': 1, 'o': 0?? }
    Wait, careful: 'l' appears 2 times in 'hello' and 1 in 'world'
    so {'h': 1, 'e': 1, 'l': 1, 'o': 0... oh, 'o' is 1 vs 1 → equal,
    skipped. 'w': -1, 'r': -1, 'd': -1}
    -> {'h': 1, 'e': 1, 'l': 1, 'w': -1, 'r': -1, 'd': -1}

    letter_diff("abc", "abc")     -> {}

Hint: Counter supports subtraction with the - operator (and
`Counter.subtract` for in-place). Note the operator's quirk:
`a - b` keeps only POSITIVE counts. You'll need both directions.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


def letter_diff(a: str, b: str) -> dict[str, int]:
    raise NotImplementedError
