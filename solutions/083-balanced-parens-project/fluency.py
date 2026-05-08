"""Rung 2: Fluency drill — fix the two near-correct balance checkers.

Topic: balanced parens with a stack.
"""


def is_balanced_simple(s: str) -> bool:
    """Return True if the string has balanced () (only this one bracket type).

    Examples:
        is_balanced_simple("(())")  -> True
        is_balanced_simple(")(")    -> False
        is_balanced_simple("(()")   -> False
    """
    stack: list[str] = []
    for ch in s:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            # TODO: this returns True instead of False on a stray ')'.
            if not stack:
                return True
            stack.pop()
    # TODO: the final answer should be True only if nothing's left over.
    return True


def matches(opener: str, closer: str) -> bool:
    """Return True iff `opener` and `closer` are a matching bracket pair."""
    pairs = {"(": ")", "[": "]", "{": "}"}
    # TODO: this checks whether the closer is in pairs (it isn't — pairs maps openers).
    return closer in pairs and pairs[closer] == opener
