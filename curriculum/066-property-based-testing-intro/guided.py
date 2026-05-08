"""Rung 3: Guided implement — encode/decode round-trip.

Topic: property-based round-trip testing.

Real-world framing: a tiny "URL-safe" encoder. Replace runs of
non-ASCII or whitespace with %XX hex escapes; restore on decode.

For learning purposes, use this simple rule:
  - Encode: bytes 0..127 that ARE alphanumeric pass through; everything
    else (including space) is replaced with `%` + 2 hex digits (uppercase).
  - Decode: reverse it.

The property is: decode(encode(s)) == s for all str.
"""


def encode(text: str) -> str:
    """Percent-encode any non-alphanumeric byte."""
    # TODO: implement.
    raise NotImplementedError


def decode(text: str) -> str:
    """Inverse of encode."""
    # TODO: implement.
    raise NotImplementedError
