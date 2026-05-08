"""Rung 3: Guided — solved version.

`roundtrip` is deliberately trivial: encode then decode. It proves that
for any string whose characters are in the given encoding's range, the
round-trip is lossless.

The interesting teaching moment is WHY this is only guaranteed for
UTF-8 (which covers all Unicode): ASCII covers only U+0000–U+007F, and
Latin-1 covers U+0000–U+00FF. "café" in ASCII would raise, but in
Latin-1 or UTF-8 it round-trips cleanly.
"""


def roundtrip(s: str, encoding: str = "utf-8") -> str:
    """Encode `s` to bytes, decode back, return the resulting str.

    >>> roundtrip("hello")
    'hello'
    >>> roundtrip("café")
    'café'
    >>> roundtrip("")
    ''
    >>> roundtrip("hello", encoding="ascii")
    'hello'
    """
    return s.encode(encoding).decode(encoding)
