"""Rung 2: Fluency drill — solved version.

The TODOs were:
  1. Greeting missing the comma + exclamation. Docstring shows the
     exact format: 'Hello, <name>!'.
  2. add_one returning n instead of n + 1.
"""


def greet(name: str) -> str:
    """Return 'Hello, <name>!' — note the comma and exclamation."""
    return f"Hello, {name}!"


def add_one(n: int) -> int:
    """Return n + 1."""
    return n + 1
