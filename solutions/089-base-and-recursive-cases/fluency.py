"""Rung 2: Fluency drill — fix the missing base cases.

Topic: recursion = base case + recursive case

Each function below recurses correctly but is missing the line that
stops it. Add the base case so it terminates and returns the right
answer for tiny inputs.
"""


def factorial(n: int) -> int:
    """Return n! (n factorial). 0! is 1."""
    # TODO: add the base case for n <= 1
    return n * factorial(n - 1)


def length(items: list) -> int:
    """Return the number of items, computed recursively."""
    # TODO: add the base case for an empty list
    return 1 + length(items[1:])
