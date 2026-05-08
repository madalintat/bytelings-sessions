"""Rung 4: Solo implement.

Topic: idiomatic Python — many idioms, one function.

Implement `top_words(text, n) -> list[tuple[str, int]]`:

  - Tokenize: split on whitespace, lowercase, strip leading/trailing
    ASCII punctuation (`!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~`).
  - Skip empty tokens.
  - Count occurrences.
  - Return the top `n` (word, count) pairs, ordered by count DESC,
    ties broken alphabetically (word ASC).
  - If `n` is 0 or negative, return [].

Idioms you'll likely use:
  - `collections.Counter` (handles count + most_common)
  - generator expressions
  - `str.strip(punctuation)` from `string.punctuation`
  - tuple unpacking in lambdas / `key=`

Hidden tests in 04_solo_test.py.
"""


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    raise NotImplementedError
