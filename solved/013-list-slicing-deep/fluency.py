"""Rung 2: Fluency — solved version.

Four slice bugs:
  1. first_n: items[-n:] gives the LAST n items. Items[:n] gives the first n.
  2. shallow_copy: `return items` returns the same object. `items[:]` (full
     slice) creates a new list with the same elements — the canonical
     one-liner for a shallow copy.
  3. replace_middle: `items[1] = replacement` does index assignment,
     replacing a single element with the list `replacement` (creating a
     nested list). SLICE assignment `items[1:3] = replacement` replaces
     the elements at indices 1 and 2 with the contents of `replacement`,
     even if `replacement` has a different length.
  4. reverse_in_place: `items[::-1]` returns a NEW reversed list. To
     mutate in place, use SLICE assignment: `items[:] = items[::-1]`.
"""


def first_n(items: list, n: int) -> list:
    """Return the first `n` items as a NEW list."""
    return items[:n]


def shallow_copy(items: list) -> list:
    """Return a shallow copy of `items` using slicing."""
    return items[:]


def replace_middle(items: list, replacement: list) -> list:
    """Replace items[1:3] in place with `replacement` and return items."""
    items[1:3] = replacement
    return items


def reverse_in_place(items: list) -> list:
    """Reverse `items` in place using slice assignment, then return items."""
    items[:] = items[::-1]
    return items
