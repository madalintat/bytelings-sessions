"""Rung 3: Guided implement — solved version.

encode: pass alphanumeric bytes through; encode everything else as
%XX uppercase hex. decode: reverse by scanning for % sequences.
The round-trip property decode(encode(s)) == s holds for all str.
"""


def encode(text: str) -> str:
    """Percent-encode any non-ASCII-alphanumeric byte.

    `ch.isalnum()` treats `é` as a letter (it is), but URL-style
    percent-encoding only passes through ASCII alnums; anything else
    becomes %XX bytes. Adding `ch.isascii()` enforces that.
    """
    out = []
    for ch in text:
        if ch.isalnum() and ch.isascii():
            out.append(ch)
        else:
            for byte in ch.encode("utf-8"):
                out.append(f"%{byte:02X}")
    return "".join(out)


def decode(text: str) -> str:
    """Inverse of encode."""
    out = []
    i = 0
    while i < len(text):
        if text[i] == "%" and i + 2 < len(text):
            byte_val = int(text[i + 1:i + 3], 16)
            out.append(byte_val)
            i += 3
        else:
            out.extend(text[i].encode("utf-8"))
            i += 1
    return bytes(out).decode("utf-8")
