"""Rung 3: Guided implement.

Topic: chunk a list using slicing

Implement `chunks(items, size)`: return a list of lists, each of
length `size`, except possibly the last.
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
    # TODO: a loop with i jumping by `size`, slicing items[i:i+size].
    raise NotImplementedError
