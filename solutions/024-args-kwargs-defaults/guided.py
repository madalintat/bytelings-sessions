"""Rung 3: Guided implement.

Topic: a function that takes any number of strings and a separator

Implement `strict_join(*parts, sep=" ", default="(empty)")`:
- Join `parts` with `sep`.
- If no parts are given, return `default`.
- Make `sep` and `default` keyword-only.
"""


def strict_join(*parts: str, sep: str = " ", default: str = "(empty)") -> str:
    """Join string parts; return `default` when no parts are given.

    >>> strict_join('a', 'b', 'c')
    'a b c'
    >>> strict_join('a', 'b', sep='-')
    'a-b'
    >>> strict_join()
    '(empty)'
    >>> strict_join(default='nothing')
    'nothing'
    >>> strict_join('only')
    'only'
    """
    # TODO: 2 lines.
    raise NotImplementedError
