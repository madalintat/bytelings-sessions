"""Rung 3: Guided implement — solved version.

Strategy: scan left-to-right for the first character that belongs to
the PEP 508 specifier set {'=', '<', '>', '!', '~'}.  Everything
before that index is the package name; everything from that index
onward is the specifier.

Whitespace handling:
- Strip the whole input first.
- Collapse any spaces inside the specifier (e.g. ">= 8.0" → ">=8.0")
  by removing all spaces from the specifier fragment.
"""
from __future__ import annotations

_SPEC_CHARS = frozenset("=<>!~")


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
    """
    req = req.strip()
    for i, ch in enumerate(req):
        if ch in _SPEC_CHARS:
            name = req[:i].strip()
            spec = req[i:].replace(" ", "")
            return name, spec
    return req, ""
