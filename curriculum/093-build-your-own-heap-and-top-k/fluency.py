"""Rung 2: Fluency drill — fix the broken sift helpers.

Topic: parent / child index math, the compare-with-smaller-child trap.
"""


def parent_index(i: int) -> int:
    """Return the parent index of `i` in a 0-indexed binary heap.

    parent(0) is conventionally 0 (no parent — it's the root).
    parent(1) is 0, parent(2) is 0, parent(3) is 1, parent(4) is 1, ...
    """
    # TODO: this is the floor of (i / 2), but heap math is (i-1) // 2.
    return i // 2


def smaller_child_index(data: list, i: int) -> int:
    """Return the index of the smaller child of `i`. If only one child
    exists, return that child. If none, return -1.

    For example, with data = [1, 3, 5, 4, 2]:
        smaller_child_index(data, 0)   # children at 1 and 2: data[1]=3, data[2]=5 -> 1
        smaller_child_index(data, 1)   # children at 3 and 4: data[3]=4, data[4]=2 -> 4
        smaller_child_index(data, 2)   # no children -> -1
    """
    n = len(data)
    left = 2 * i + 1
    right = 2 * i + 2
    if left >= n:
        return -1
    # TODO: this always picks left, ignoring whether right is smaller.
    return left
