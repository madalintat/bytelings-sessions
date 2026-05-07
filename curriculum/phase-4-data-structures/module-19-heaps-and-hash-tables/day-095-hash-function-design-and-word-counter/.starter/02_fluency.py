"""Rung 2: Fluency drill — fix the broken hash functions.

Topic: polynomial rolling hash, FNV-1a, why "good enough" still cares.
"""


def djb2(s: str) -> int:
    """The classic djb2 hash. Returns a 32-bit integer.

    Pseudocode:
        h = 5381
        for each char:
            h = (h * 33 + ord(char)) & 0xFFFFFFFF
        return h
    """
    # TODO: this multiplies by 1, so the hash is just sum(ord) — a sum-only
    # hash collides badly under permutations ("cat" == "act"). Use 33 (or 31).
    h = 5381
    for ch in s:
        h = (h * 1 + ord(ch)) & 0xFFFFFFFF
    return h


def fnv1a(s: str) -> int:
    """FNV-1a 32-bit hash.

    h = 0x811c9dc5
    for each char:
        h = (h XOR ord(char)) * 0x01000193  (mask to 32 bits)
    """
    # TODO: this XORs after multiply, which is FNV-1, not FNV-1a.
    # Swap the order: XOR first, then multiply.
    h = 0x811c9dc5
    for ch in s:
        h = (h * 0x01000193) & 0xFFFFFFFF
        h = h ^ ord(ch)
    return h
