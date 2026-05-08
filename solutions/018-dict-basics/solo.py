"""Rung 4: Solo implement.

Topic: invert a dict

Implement `invert(d)`:

- Take a dict {key: value} and return {value: key}.
- If multiple keys map to the same value, only ONE wins — the LATEST
  one (the one inserted last).
- Empty dict -> empty dict.
- Values must be hashable (don't worry about non-hashable values; the
  tests only use hashable values).

Examples:
    invert({'a': 1, 'b': 2})    -> {1: 'a', 2: 'b'}
    invert({'a': 1, 'b': 1})    -> {1: 'b'}     # last wins
    invert({})                  -> {}

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


def invert(d: dict) -> dict:
    raise NotImplementedError
