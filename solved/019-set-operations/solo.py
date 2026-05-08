"""Rung 4: Solo — solved version.

`anagram_groups` groups words by their sorted-char tuple, which is the
canonical hashable key for "same letters, same counts":
  - `tuple(sorted(word))` produces e.g. ('a', 'e', 't') for "eat", "tea", "ate".
  - A `dict` keyed by this tuple accumulates the groups.
  - The output list is built from dict.values() — insertion order is preserved
    in Python 3.7+, so groups appear in first-seen order.

Using a plain dict (not defaultdict) with a check is fine here; `defaultdict(list)`
is also perfectly idiomatic (Day 20 covers it).
"""
from collections import defaultdict


def anagram_groups(words: list[str]) -> list[list[str]]:
    groups: dict[tuple, list[str]] = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)
    return list(groups.values())
