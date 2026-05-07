"""Rung 3: Guided implement.

Topic: round-trip a string through bytes

Implement `roundtrip(s, encoding)`: encode `s`, then decode the bytes
back, returning the result. Should be equal to `s` for any UTF-8.
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
    # TODO: 2 lines: encode, then decode.
    raise NotImplementedError
