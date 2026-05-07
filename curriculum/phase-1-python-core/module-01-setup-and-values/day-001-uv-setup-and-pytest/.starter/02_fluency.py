"""Rung 2: Fluency drill — fix the two broken bits.

Topic: pytest basics + Python expressions

The watcher runs the tests in 02_fluency_test.py on every save. Your
job is to make all of them pass.
"""


def greet(name: str) -> str:
    """Return 'Hello, <name>!' — note the comma and exclamation."""
    # TODO: this string is missing the punctuation
    return f"Hello {name}"


def add_one(n: int) -> int:
    """Return n + 1."""
    # TODO: off-by-one error
    return n
