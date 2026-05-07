"""Rung 2: Fluency drill — fix the two broken stack helpers.

Topic: stack push/pop on a list, the right end vs the wrong end.
"""


def push_all(stack: list, items: list) -> None:
    """Push each item from `items` onto `stack` (in order, last-pushed-on-top)."""
    # TODO: this is using the WRONG end of the list — fix it.
    for item in items:
        stack.insert(0, item)


def pop_top(stack: list):
    """Remove and return the top of the stack. Raise IndexError if empty."""
    # TODO: pop() with no argument is the right one for a stack.
    return stack.pop(0)
