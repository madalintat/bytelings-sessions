"""Rung 2: Fluency drill — fix the broken regex patterns.

Topic: re basics
"""
import re


def is_us_zip(s: str) -> bool:
    """Return True iff `s` is exactly 5 digits."""
    # TODO: this matches ANY string starting with 5 digits, including '12345abc'
    return re.match(r"\d{5}", s) is not None


def find_words(s: str) -> list[str]:
    """Return every run of word-characters (letters/digits/underscore) in `s`."""
    # TODO: + needed; '\w' alone matches single chars
    return re.findall(r"\w", s)


def is_hex_color(s: str) -> bool:
    """Return True iff `s` is like '#abc' or '#aabbcc' (3 or 6 hex digits)."""
    # TODO: pattern doesn't allow the 6-digit form, and isn't anchored
    return re.fullmatch(r"#[0-9a-fA-F]{3}", s) is not None


def replace_digits(s: str) -> str:
    """Replace each run of digits with '#' (one '#' per run, not per digit)."""
    # TODO: + missing; this replaces each digit individually
    return re.sub(r"\d", "#", s)
