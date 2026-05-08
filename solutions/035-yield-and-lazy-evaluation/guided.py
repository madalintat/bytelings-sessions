"""Rung 3: Guided implement.

Topic: a streaming generator with state

Implement `chunked(iterable, size)` — yield successive lists of length
`size` from the iterable. The last chunk may be shorter if there
aren't enough items.

>>> list(chunked([1, 2, 3, 4, 5], 2))
[[1, 2], [3, 4], [5]]
>>> list(chunked([], 3))
[]
"""


def chunked(iterable, size: int):
    """Yield consecutive sublists of length up to `size`.

    Behavior:
        - If size <= 0, raise ValueError.
        - If iterable is empty, yield nothing.
        - The last yielded chunk may have fewer than `size` items.
    """
    # TODO: implement.
    # Hint: build a buffer list, append until len == size, yield it,
    # reset buffer. After the loop, yield the leftover if non-empty.
    raise NotImplementedError
