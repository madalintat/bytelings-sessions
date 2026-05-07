"""Rung 4: Solo.

Topic: case-insensitive sort with stability for case-tiebreakers.

Implement `nice_sort(words)`:
- Sort words alphabetically, case-insensitive.
- BUT when two words are equal ignoring case, the one originally first
  in the input must come first in the output (rely on stability).

>>> nice_sort(["Banana", "apple", "banana", "Apple"])
['apple', 'Apple', 'Banana', 'banana']

(In the input, "apple" came before "Apple", so "apple" wins the tie
in the output. Same for "Banana" vs "banana".)

Tests in 04_solo_test.py are HIDDEN.
"""


def nice_sort(words: list[str]) -> list[str]:
    raise NotImplementedError
