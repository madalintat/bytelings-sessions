"""Rung 2: Fluency — solved version.

The TODO described a silent mutation: `lst.append(item)` modifies
the caller's list in place. The docstring says "return a NEW list
with item appended; do not mutate the input."

Two idioms work:

  Slice copy + append (clear about the copy):
      copy = lst[:]
      copy.append(item)
      return copy

  Concatenation (one-liner; allocates fresh):
      return lst + [item]

  Spread (Python 3.5+):
      return [*lst, item]

The concatenation form is the most idiomatic — `+` on lists always
returns a new list, so there's no mutation risk by construction.
"""


def append_safely(lst: list, item) -> list:
    """Return a NEW list with item appended; do not mutate the input."""
    return lst + [item]
