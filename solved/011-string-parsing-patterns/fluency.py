"""Rung 2: Fluency — solved version.

Three parsing pattern fixes:
  1. csv_fields: str.split(',') doesn't strip whitespace from pieces.
     Chain a comprehension: [p.strip() for p in line.split(',')].
  2. keep_digits: using `return` inside the loop returns on the FIRST
     match instead of collecting all digits. Use a generator expression
     and join: ''.join(c for c in s if c.isdigit()).
  3. split_on_any: str.split(seps) splits on the whole multi-character
     separator as a unit, not on any individual character in it. Use
     re.split with a character class instead: re.split(f'[{re.escape(seps)}]', s).
"""
import re


def csv_fields(line: str) -> list[str]:
    """Split on commas and strip each piece."""
    return [p.strip() for p in line.split(",")]


def keep_digits(s: str) -> str:
    """Return only the digit characters of `s`, in order."""
    return "".join(c for c in s if c.isdigit())


def split_on_any(s: str, seps: str) -> list[str]:
    """Split `s` on ANY char appearing in `seps`. Drop empty pieces.

    Example: split_on_any('a, b; c', ',;') -> ['a', 'b', 'c']
    """
    return [p.strip() for p in re.split(f"[{re.escape(seps)}]", s) if p.strip()]
