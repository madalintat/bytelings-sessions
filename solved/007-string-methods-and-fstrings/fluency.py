"""Rung 2: Fluency — solved version.

Four str-method traps:
  1. normalize: .lower() doesn't strip — chain strip().lower() (order matters:
     strip first so you don't lowercase before catching the whitespace).
     Actually either order works here; strip then lower is idiomatic.
  2. join_words: str.join is called on the SEPARATOR, not the list.
     Correct form: " ".join(words), not words.join(" ").
  3. format_price: f-string format spec `:.2f` forces exactly two decimal
     places. Without it, 9.5 prints as "9.5" instead of "9.50".
  4. is_csv_line: str.endswith is case-sensitive. Use .lower() on the
     suffix or call endswith on the lowercased string.
"""


def normalize(s: str) -> str:
    """Return `s` with surrounding whitespace removed and lowercased."""
    return s.strip().lower()


def join_words(words: list[str]) -> str:
    """Join words with a single space between them."""
    return " ".join(words)


def format_price(qty: int, price: float) -> str:
    """Return e.g. '3 items at $9.50' — note exactly 2 decimals."""
    return f"{qty} items at ${price:.2f}"


def is_csv_line(s: str) -> bool:
    """Return True if `s` ends with '.csv' (case-insensitive)."""
    return s.lower().endswith(".csv")
