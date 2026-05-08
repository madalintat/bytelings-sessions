"""Rung 2: Fluency drill — rewrite three functions Pythonically.

Topic: idiomatic Python.

Each function below works correctly but is written in an awkward,
non-Pythonic style. Rewrite the BODIES to use idiomatic Python.
The behavior must not change. The tests run a smoke check AND a
structural check (e.g., "must use enumerate", "must use a comprehension").
"""


def indexed(items: list[str]) -> list[tuple[int, str]]:
    """Pair each item with its index. Use enumerate, not range(len(...))."""
    out = []
    for i in range(len(items)):
        out.append((i, items[i]))
    return out


def squares(xs: list[int]) -> list[int]:
    """Square each x. Use a list comprehension."""
    out = []
    for x in xs:
        out.append(x * x)
    return out


def is_empty(name: str) -> bool:
    """True if name is empty. Use truthiness, not == ""."""
    if name == "":
        return True
    else:
        return False
