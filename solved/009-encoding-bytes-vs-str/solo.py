"""Rung 4: Solo — solved version.

`count_chars` decodes the bytes blob with the specified encoding,
using errors="replace" so that invalid bytes become U+FFFD (one
character each). Then `len()` of the resulting str is the character
count.

Key insight: `len(b)` would give BYTE count. `len(b.decode(..., errors="replace"))`
gives CHAR count, which is what the spec asks for. Each invalid byte is
replaced by a single character, so the count is still well-defined.
"""


def count_chars(b: bytes, encoding: str = "utf-8") -> int:
    return len(b.decode(encoding, errors="replace"))
