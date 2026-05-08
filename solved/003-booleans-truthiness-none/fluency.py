"""Rung 2: Fluency — solved version.

The TODOs were three flavors of the same family of bugs: confusing
*truthiness* (does Python treat this as falsy?) with *None-ness*
(is this specifically None?) and *equality* (==) with *identity* (is).

  1. has_value: `bool(x)` says False for "", [], 0, None — too broad.
     The right check is `x is not None`.
  2. is_blank_string: `s is ""` happens to work in CPython because
     small strings get interned, but it's still semantically wrong
     and warns in 3.8+. Compare strings by value with `==`.
  3. is_definitely_false: `x == False` is True for 0 and [] (because
     False == 0 in Python). To match the LITERAL `False` object,
     use `x is False`.

The "is" vs "==" choice is the day's deepest concept: `is` checks
*the same object*, `==` checks *equal value*. They overlap for
small ints, None, True/False (because Python interns those) — but
relying on overlap is the bug.
"""


def has_value(x) -> bool:
    """Return True if x is not None (regardless of truthiness)."""
    return x is not None


def is_blank_string(s: str) -> bool:
    """Return True if s is an empty string."""
    return s == ""


def is_definitely_false(x) -> bool:
    """Return True if x is the literal False (not 0, not None, not '')."""
    return x is False
