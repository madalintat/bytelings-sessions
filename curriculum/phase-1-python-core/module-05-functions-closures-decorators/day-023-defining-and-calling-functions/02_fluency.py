"""Rung 2: Fluency drill — function shapes.

Topic: signatures, defaults, keyword-only
"""


def greet(name, greeting="Hello"):
    """Return f'{greeting}, {name}!'.

    Make `greeting` keyword-only by adding `*` in the signature.
    Add type hints (str, str) and a return-type hint (str).
    """
    # TODO: signature shape; body is correct
    return f"{greeting}, {name}!"


def clamp(x, lo, hi):
    """Constrain x to [lo, hi]. Add type hints (float, float, float -> float)."""
    # TODO: this `if` ladder is correct but ugly; rewrite as one line:
    #   return max(lo, min(x, hi))
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x


def add_to_list(item, container=[]):
    """Append `item` to `container` and return it.

    The default-mutable-arg here is a known trap (preview of Day 24).
    For now, fix this signature so the default is None and we build a
    new list inside if the caller didn't pass one.
    """
    # TODO: default mutable arg; switch to None + lazy create
    container.append(item)
    return container
