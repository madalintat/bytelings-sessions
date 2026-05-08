"""Rung 3: Guided — solved version.

`chunks` splits a list into sub-lists of `size` using a strided range loop.
The idiom `range(0, len(items), size)` produces starting indices 0, size,
2*size, ... and `items[i : i+size]` slices each chunk. The last chunk may
be shorter than `size` — Python slicing handles this gracefully by capping
at the end of the list.

Raising ValueError for size <= 0 prevents an infinite loop (range with
step 0 raises, but step < 0 would loop backward).
"""


def chunks(items: list, size: int) -> list[list]:
    """Split `items` into consecutive chunks of `size`.

    >>> chunks([1, 2, 3, 4, 5, 6, 7], 3)
    [[1, 2, 3], [4, 5, 6], [7]]
    >>> chunks([], 3)
    []
    >>> chunks([1, 2], 5)
    [[1, 2]]

    Raise ValueError if `size <= 0`.
    """
    if size <= 0:
        raise ValueError(f"size must be > 0, got {size}")
    return [items[i : i + size] for i in range(0, len(items), size)]
