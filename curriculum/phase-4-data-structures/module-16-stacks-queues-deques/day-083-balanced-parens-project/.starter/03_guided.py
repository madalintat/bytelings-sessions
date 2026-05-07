"""Rung 3: Guided implement — a precise balance checker.

Topic: a stack-driven validator that returns a useful error report.
"""
from typing import NamedTuple, Optional


class Problem(NamedTuple):
    """A single bracket problem in the input.

    kind:    one of "stray-closer", "mismatched", "unclosed"
    index:   character index in the input string where the problem was detected
    char:    the character at `index`
    """
    kind: str
    index: int
    char: str


def check_brackets(s: str) -> Optional[Problem]:
    """Validate that all (), [], {} brackets in `s` are properly nested.

    Returns None if balanced. Otherwise returns a Problem describing the
    FIRST issue found while scanning left to right. Possible kinds:

    - "stray-closer": a closing bracket appeared with no matching open.
        check_brackets("ab)cd")
        -> Problem("stray-closer", 2, ")")

    - "mismatched": a closing bracket doesn't match the most recent open.
        check_brackets("([)]")
        -> Problem("mismatched", 2, ")")

    - "unclosed": end of input with openers still on the stack.
        The index points to the most recently UNCLOSED opener.
        check_brackets("([")
        -> Problem("unclosed", 1, "[")

    Non-bracket characters are ignored.
    """
    pairs = {")": "(", "]": "[", "}": "{"}
    openers = set("([{")
    closers = set(")]}")
    # TODO: walk the string keeping a stack of (opener_char, opener_index).
    # On each character:
    #   - if opener:  push (char, index)
    #   - if closer and stack empty:  return Problem("stray-closer", index, char)
    #   - if closer and top doesn't match:  return Problem("mismatched", index, char)
    #   - if closer and matches:  pop
    # After the loop:
    #   - if stack non-empty:  pick the top, return Problem("unclosed", that_index, that_char)
    #   - else:  return None
    raise NotImplementedError
