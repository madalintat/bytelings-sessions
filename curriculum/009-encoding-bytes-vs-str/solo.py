"""Rung 4: Solo implement.

Topic: count UTF-8 characters in a bytes blob safely

Implement `count_chars(b, encoding="utf-8")`:

- Decode `b` using `encoding` with errors="replace" (so it never crashes).
- Return the number of characters (code points) in the resulting str.
- An invalid byte is "replaced" with one char (U+FFFD) — count it as 1.

The tests in 04_solo_test.py are HIDDEN. Don't peek before you try.
"""


def count_chars(b: bytes, encoding: str = "utf-8") -> int:
    raise NotImplementedError
