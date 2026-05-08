"""Rung 2: Fluency — solved version.

djb2: the stub multiplies by 1 (effectively summing ordinals), which
  means "cat" and "act" produce the same hash. The classic djb2
  multiplier is 33. Change `h * 1` to `h * 33`.

fnv1a: the stub applies XOR AFTER multiply, which is FNV-1 (not
  FNV-1a). FNV-1a XORs FIRST, then multiplies. Swap the two lines
  inside the loop.
"""


def djb2(s: str) -> int:
    """Classic djb2 hash. Returns a 32-bit integer."""
    h = 5381
    for ch in s:
        h = (h * 33 + ord(ch)) & 0xFFFFFFFF
    return h


def fnv1a(s: str) -> int:
    """FNV-1a 32-bit hash: XOR first, then multiply."""
    h = 0x811c9dc5
    for ch in s:
        h = (h ^ ord(ch)) * 0x01000193 & 0xFFFFFFFF
    return h
