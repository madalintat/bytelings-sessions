"""Rung 4: Solo implement.

Topic: write `top_words(text, k)` — the k most common words, with
ties broken alphabetically.

Given a text string and a positive int k, return a list of (word, count)
tuples sorted by:
    1. count, descending
    2. word, ascending  (i.e. "apple" before "banana" when counts tie)

Words are runs of [a-zA-Z'], case-folded to lowercase. (Use the same
rule as rung 3's word_counts.)

Examples:
    top_words("a b a c b a", 2)
    -> [("a", 3), ("b", 2)]

    top_words("a b c d", 10)
    -> [("a", 1), ("b", 1), ("c", 1), ("d", 1)]   # all four, sorted

    top_words("", 5)
    -> []

This is what most "top-k" CLIs ship. The implementation is one
counts-collect, one sort, one slice — but you choose the sort key
carefully so ties are deterministic.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.

Patterns: P-03 (walrus-in-condition), P-07 (accumulator-into-dict), P-10 (visit-set-for-dedup), P-31 (string-build-via-list-then-join).
"""


def top_words(text: str, k: int) -> list[tuple[str, int]]:
    raise NotImplementedError
