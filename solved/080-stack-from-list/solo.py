"""Rung 4: Solo implement — solved version.

Push every character onto a stack (list), then pop them all and join.
This demonstrates the LIFO property producing reversal naturally.
"""


def reverse_string(s: str) -> str:
    stack: list[str] = []
    for ch in s:
        stack.append(ch)
    result = []
    while stack:
        result.append(stack.pop())
    return "".join(result)
