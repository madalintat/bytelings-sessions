"""Rung 4: Solo implement — solved version.

Idiomatic Python: a generator expression inside sum() counts the
truthy values. `c.lower() in 'aeiou'` handles case-insensitivity in
one shot; non-letters fall through naturally because they're not in
the vowel set. Empty string returns 0 because sum() of an empty
generator is 0.

Patterns exercised: P-01 (sentinel-loop is one mental model;
sum-of-truthy is its more Pythonic cousin).
"""


def count_vowels(text: str) -> int:
    return sum(1 for c in text if c.lower() in "aeiou")
