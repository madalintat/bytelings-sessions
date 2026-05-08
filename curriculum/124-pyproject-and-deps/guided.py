"""Rung 3: Guided implement.

Topic: parsing PEP 508 requirement strings

A requirement string like 'click>=8.1' has a name ('click') and a
specifier ('>=8.1'). We won't write a full PEP 508 parser — that's a
real library's job. We just split on the first specifier character.

Fill in the body. Use only stdlib.
"""
from __future__ import annotations


def split_requirement(req: str) -> tuple[str, str]:
    """Split 'name<specifier>' into (name, specifier).

    Specifier characters are any of: == != >= <= > < ~= !=

    Examples:
        >>> split_requirement("click>=8.1")
        ('click', '>=8.1')
        >>> split_requirement("rich")
        ('rich', '')
        >>> split_requirement("httpx==0.27.0")
        ('httpx', '==0.27.0')
        >>> split_requirement("  pytest >= 8.0  ")
        ('pytest', '>=8.0')

    Whitespace inside the requirement is collapsed in the specifier.
    Leading/trailing whitespace on the whole string is stripped.
    """
    # TODO: scan for the first character in '=<>!~', split there,
    # strip both sides, then strip any internal whitespace from the spec.
    raise NotImplementedError
