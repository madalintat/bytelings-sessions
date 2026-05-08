"""Rung 3: Guided — solved version.

`strict_join` uses `*parts` to collect any number of positional strings,
and keyword-only `sep` and `default` (after the `*parts`).

Logic:
  - If no parts were given (`not parts`), return `default`.
  - Otherwise `sep.join(parts)`.

The keyword-only constraint: everything after `*parts` in the signature
is automatically keyword-only. So `sep` and `default` can only be passed
as `sep=`, `default=` — positional passing is not possible.
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
    if not parts:
        return default
    return sep.join(parts)
