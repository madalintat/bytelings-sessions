"""Rung 3: Guided implement — solved version.

Walk the string once. Push (char, index) for openers. On a closer:
- empty stack -> "stray-closer"
- top doesn't match -> "mismatched"
- matches -> pop
After the walk, the topmost unpopped opener is "unclosed". None if balanced.
"""
from typing import NamedTuple, Optional


class Problem(NamedTuple):
    kind: str
    index: int
    char: str


def check_brackets(s: str) -> Optional[Problem]:
    """Validate that all (), [], {} brackets in `s` are properly nested."""
    pairs = {")": "(", "]": "[", "}": "{"}
    openers = set("([{")
    closers = set(")]}")
    stack: list[tuple[str, int]] = []

    for i, ch in enumerate(s):
        if ch in openers:
            stack.append((ch, i))
        elif ch in closers:
            if not stack:
                return Problem("stray-closer", i, ch)
            top_char, top_idx = stack[-1]
            if top_char != pairs[ch]:
                return Problem("mismatched", i, ch)
            stack.pop()

    if stack:
        top_char, top_idx = stack[-1]
        return Problem("unclosed", top_idx, top_char)
    return None
