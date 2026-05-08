"""Rung 4: Solo implement.

Topic: find anagram groups using a frozenset-friendly key

Implement `anagram_groups(words)`:

- Take a list of strings.
- Return a list of lists, where each inner list is a group of anagrams
  of each other (words with the same letter multiset).
- Each group should contain words IN THE ORDER they first appeared.
- The OUTER list is ordered by the first-seen anagram of each group.
- A 'group' of size 1 still counts (a unique word forms its own group).

Examples:
    anagram_groups(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
    -> [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    anagram_groups([])  -> []

Hint: a sorted-tuple-of-chars makes a hashable group key.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.

Patterns: P-07 (accumulator-into-dict), P-10 (visit-set-for-dedup).
"""


def anagram_groups(words: list[str]) -> list[list[str]]:
    raise NotImplementedError
