"""Rung 3: Guided — solved version.

`repeat_word` is the canonical str.join use case:
  - Build a list of `times` copies with `[word] * times` (O(1) list
    construction, since it's a list of references to the same string).
  - Call `sep.join(...)` once to concatenate.

This is O(n) in the output length, which is the best you can do.
The starter hint mentions `[word] * times` — that's idiomatic here
and avoids an explicit loop. `sep.join([word] * 0)` correctly returns "".

Alternative using a generator:
    sep.join(word for _ in range(times))
is also correct but slightly slower and less readable than `[word] * times`.
"""


def repeat_word(word: str, sep: str, times: int) -> str:
    """Return `word` repeated `times` times, separated by `sep`.

    >>> repeat_word("hi", "-", 3)
    'hi-hi-hi'
    >>> repeat_word("x", ", ", 0)
    ''
    >>> repeat_word("x", ", ", 1)
    'x'
    >>> repeat_word("", "-", 3)
    '--'
    """
    return sep.join([word] * times)
