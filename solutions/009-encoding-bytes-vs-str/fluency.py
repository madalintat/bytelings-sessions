"""Rung 2: Fluency drill — fix the encode/decode bugs.

Topic: bytes vs str, UTF-8
"""


def to_bytes(s: str) -> bytes:
    """Encode `s` as UTF-8 bytes."""
    # TODO: encoding name is wrong (and the call too)
    return s.encode("ascii")


def from_bytes(b: bytes) -> str:
    """Decode UTF-8 `b` back to a str."""
    # TODO: bytes have a .decode method, not bytes(...)
    return bytes(b)


def byte_length(s: str) -> int:
    """Return how many BYTES `s` takes in UTF-8 (not how many chars)."""
    # TODO: len(s) gives chars, not bytes
    return len(s)


def safe_decode(b: bytes) -> str:
    """Decode `b` as UTF-8; if a byte is invalid, replace it (don't crash)."""
    # TODO: errors policy is missing
    return b.decode("utf-8")
