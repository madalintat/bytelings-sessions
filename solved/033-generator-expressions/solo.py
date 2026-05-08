"""Rung 4: Solo — solved version.

We cannot materialise the whole input (`strings` may be a generator).
The trick is to pair each string with its index *before* sorting, using
`enumerate`. `sorted()` accepts any iterable and pulls it lazily; we
sort by `(-length, index)` so the longest strings come first and ties
are broken by earlier position. We then take the first `n` results and
strip the metadata.
"""


def top_n_lengths(strings, n: int) -> list[int]:
    if n <= 0:
        return []
    pairs = sorted(
        ((-len(s), i, len(s)) for i, s in enumerate(strings)),
        key=lambda t: (t[0], t[1]),
    )
    return [length for _, _, length in pairs[:n]]
