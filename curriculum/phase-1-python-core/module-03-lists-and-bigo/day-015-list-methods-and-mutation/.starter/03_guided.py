"""Rung 3: Guided implement.

Topic: sort with a key

Implement `sort_by_length(strings, *, descending=False)`: return a new
list of strings sorted by length. Ties keep their original order
(sorted is stable in Python).
"""


def sort_by_length(strings: list[str], descending: bool = False) -> list[str]:
    """Return a new list sorted by string length.

    >>> sort_by_length(["bee", "a", "carrot"])
    ['a', 'bee', 'carrot']
    >>> sort_by_length(["bee", "a", "carrot"], descending=True)
    ['carrot', 'bee', 'a']
    >>> sort_by_length(["aa", "bb", "cc"])
    ['aa', 'bb', 'cc']

    Use the built-in `sorted()` with a key function. Don't mutate input.
    """
    # TODO: one line — sorted(strings, key=len, reverse=descending)
    raise NotImplementedError
