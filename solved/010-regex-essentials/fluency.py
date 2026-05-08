"""Rung 2: Fluency — solved version.

Four regex bugs:
  1. is_us_zip: `re.match(r"\\d{5}", s)` matches any string that STARTS
     with 5 digits, including "12345abc". Adding `$` (or using
     `re.fullmatch`) anchors the end of string. `re.fullmatch` is
     cleaner because it anchors both ends implicitly.
  2. find_words: `\\w` matches a SINGLE word character. `\\w+` matches
     one or more, giving whole words/tokens.
  3. is_hex_color: the pattern `#[0-9a-fA-F]{3}` only matches 3-digit
     forms. The 6-digit form needs alternation: `{3}|{6}` or
     `{3}(?:[0-9a-fA-F]{3})?`.  Using `re.fullmatch` handles anchoring.
  4. replace_digits: `\\d` matches one digit, replacing each one with "#".
     `\\d+` matches a RUN of digits, replacing the whole run with one "#".
"""
import re


def is_us_zip(s: str) -> bool:
    """Return True iff `s` is exactly 5 digits."""
    return re.fullmatch(r"\d{5}", s) is not None


def find_words(s: str) -> list[str]:
    """Return every run of word-characters (letters/digits/underscore) in `s`."""
    return re.findall(r"\w+", s)


def is_hex_color(s: str) -> bool:
    """Return True iff `s` is like '#abc' or '#aabbcc' (3 or 6 hex digits)."""
    return re.fullmatch(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?", s) is not None


def replace_digits(s: str) -> str:
    """Replace each run of digits with '#' (one '#' per run, not per digit)."""
    return re.sub(r"\d+", "#", s)
