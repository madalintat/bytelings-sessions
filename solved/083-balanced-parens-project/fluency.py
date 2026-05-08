"""Rung 2: Fluency drill — solved version.

is_balanced_simple: on stray closer return False (not True); after the
loop return `not stack` (True only if nothing's left over).
matches: checks pairs[opener] == closer, not closer in pairs.
"""


def is_balanced_simple(s: str) -> bool:
    """Return True if the string has balanced () only."""
    stack: list[str] = []
    for ch in s:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if not stack:
                return False
            stack.pop()
    return not stack


def matches(opener: str, closer: str) -> bool:
    """Return True iff `opener` and `closer` are a matching bracket pair."""
    pairs = {"(": ")", "[": "]", "{": "}"}
    return opener in pairs and pairs[opener] == closer
