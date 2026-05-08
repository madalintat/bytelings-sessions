"""Rung 3: Guided implement.

Topic: build a string in O(n), not O(n^2)

Implement `repeat_word(word, sep, times)`: return `sep`-separated
copies of `word`, joined `times` times. Use `str.join`.
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
    # TODO: build a list of `times` copies, then sep.join it.
    # Hint: a list literal `[word] * times` is one way.
    raise NotImplementedError
