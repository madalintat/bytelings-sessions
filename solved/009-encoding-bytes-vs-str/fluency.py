"""Rung 2: Fluency — solved version.

Four encoding bugs:
  1. to_bytes: "ascii" can't encode non-ASCII characters like 'é'.
     Use "utf-8", which is the universal default for Python 3.
  2. from_bytes: `bytes(b)` does NOT decode — it copies the bytes object.
     Bytes have a `.decode(encoding)` method, mirroring `str.encode()`.
  3. byte_length: `len(s)` counts Unicode code points (chars), not bytes.
     UTF-8 may use 1–4 bytes per char. `len(s.encode("utf-8"))` gives bytes.
  4. safe_decode: the `errors` keyword controls what happens on invalid
     bytes. "replace" substitutes U+FFFD (the replacement character) for
     each bad byte, so the call never raises UnicodeDecodeError.
"""


def to_bytes(s: str) -> bytes:
    """Encode `s` as UTF-8 bytes."""
    return s.encode("utf-8")


def from_bytes(b: bytes) -> str:
    """Decode UTF-8 `b` back to a str."""
    return b.decode("utf-8")


def byte_length(s: str) -> int:
    """Return how many BYTES `s` takes in UTF-8 (not how many chars)."""
    return len(s.encode("utf-8"))


def safe_decode(b: bytes) -> str:
    """Decode `b` as UTF-8; if a byte is invalid, replace it (don't crash)."""
    return b.decode("utf-8", errors="replace")
