"""Rung 2: Fluency drill — solved version.

push_all uses list.append (the right end of the list for stack semantics).
pop_top uses list.pop() with no argument (also the right end), which is O(1).
Using insert(0, ...) and pop(0) are the O(n) anti-patterns.
"""


def push_all(stack: list, items: list) -> None:
    """Push each item from `items` onto `stack` (in order, last-pushed-on-top)."""
    for item in items:
        stack.append(item)


def pop_top(stack: list):
    """Remove and return the top of the stack. Raise IndexError if empty."""
    return stack.pop()
