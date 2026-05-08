"""Rung 3: Guided — solved version.

The buffer pattern: accumulate items into a list; when it fills to
`size`, yield the buffer and reset. After the loop, yield whatever
remains. We use `list(buffer)` to yield a snapshot — if we yielded
`buffer` directly and then cleared it, the caller would see an empty
list.
"""


def chunked(iterable, size: int):
    """Yield consecutive sublists of length up to `size`.

    >>> list(chunked([1, 2, 3, 4, 5], 2))
    [[1, 2], [3, 4], [5]]
    >>> list(chunked([], 3))
    []
    """
    if size <= 0:
        raise ValueError(f"size must be > 0, got {size}")
    buffer = []
    for item in iterable:
        buffer.append(item)
        if len(buffer) == size:
            yield list(buffer)
            buffer.clear()
    if buffer:
        yield buffer
