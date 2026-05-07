"""Rung 3: Guided implement.

Topic: count occurrences with a dict

Implement `word_count(text)`: a dict mapping each word to how many
times it appears in `text`. Words are split on whitespace.
"""


def word_count(text: str) -> dict[str, int]:
    """Count words by occurrence.

    Words are split on whitespace (str.split() with no args).
    Words are CASE-SENSITIVE: 'The' and 'the' are different.

    >>> word_count("the cat sat on the mat")
    {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
    >>> word_count("")
    {}
    >>> word_count("a a a")
    {'a': 3}

    Use the `d[k] = d.get(k, 0) + 1` idiom.
    """
    # TODO: 4 lines.
    raise NotImplementedError
