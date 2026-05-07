"""Rung 2: Fluency drill — fix the broken string-method calls.

Topic: str methods + f-strings
"""


def normalize(s: str) -> str:
    """Return `s` with surrounding whitespace removed and lowercased."""
    # TODO: missing the strip step
    return s.lower()


def join_words(words: list[str]) -> str:
    """Join words with a single space between them."""
    # TODO: join is called on the separator, not the list
    return words.join(" ")


def format_price(qty: int, price: float) -> str:
    """Return e.g. '3 items at $9.50' — note exactly 2 decimals."""
    # TODO: format spec is missing
    return f"{qty} items at ${price}"


def is_csv_line(s: str) -> bool:
    """Return True if `s` ends with '.csv' (case-insensitive)."""
    # TODO: not case-insensitive
    return s.endswith(".csv")
