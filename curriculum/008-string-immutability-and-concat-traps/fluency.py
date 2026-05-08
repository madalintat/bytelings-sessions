"""Rung 2: Fluency drill — the immutability traps.

Topic: strings are immutable; methods don't mutate; join over +=
"""


def shout(s: str) -> str:
    """Return `s` uppercased."""
    # TODO: methods don't mutate; this returns the unchanged input
    s.upper()
    return s


def join_with_dashes(words: list[str]) -> str:
    """Join `words` with '-' between them, in O(n)."""
    # TODO: O(n^2) string concat; use join instead
    out = ""
    for i, w in enumerate(words):
        if i > 0:
            out += "-"
        out += w
    return out


def replace_spaces(s: str) -> str:
    """Replace every space with '_'."""
    # TODO: replace returns a new string; the original is unchanged
    s.replace(" ", "_")
    return s
