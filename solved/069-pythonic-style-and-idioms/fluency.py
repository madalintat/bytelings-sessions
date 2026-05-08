"""Rung 2: Fluency drill — solved version.

Each function rewritten with the idiomatic Python pattern:
- indexed: enumerate instead of range(len(...))
- squares: list comprehension instead of append loop
- is_empty: truthiness test instead of == ""
"""


def indexed(items: list[str]) -> list[tuple[int, str]]:
    """Pair each item with its index. Use enumerate, not range(len(...))."""
    return list(enumerate(items))


def squares(xs: list[int]) -> list[int]:
    """Square each x. Use a list comprehension."""
    return [x * x for x in xs]


def is_empty(name: str) -> bool:
    """True if name is empty. Use truthiness, not == ""."""
    return not name
