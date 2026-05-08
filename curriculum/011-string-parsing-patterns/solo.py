"""Rung 4: Solo implement.

Topic: parse a 'KEY=value' env-file-like blob into a dict

Implement `parse_env(text)`:

- Input is multi-line text. One assignment per line.
- Each line is 'KEY=value'.
- Lines that are empty (or only whitespace) are skipped.
- Lines that start with '#' (after stripping leading whitespace) are
  comments and skipped.
- Keys and values may have surrounding whitespace; strip both.
- Values may contain '=' (only split on the FIRST '=').
- If a line has no '=', skip it silently.
- Later assignments overwrite earlier ones.

Return a dict {key: value}.

Example:
    'A=1\nB = two\n# comment\nC=eq=ok' -> {'A': '1', 'B': 'two', 'C': 'eq=ok'}

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.

Patterns: P-01 (sentinel-loop).
"""


def parse_env(text: str) -> dict[str, str]:
    raise NotImplementedError
