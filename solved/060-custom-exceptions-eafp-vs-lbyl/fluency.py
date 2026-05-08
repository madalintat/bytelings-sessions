"""Rung 2: Fluency — solved version.

EAFP: attempt the operation (`parts[0]`), catch the specific exception
(`IndexError`) that fires when the list is empty. The LBYL version had
a redundant `if parts[0] is None` branch that could never be True for
`str.split()` output — EAFP eliminates the dead code.
"""


def first_word(text: str) -> str:
    try:
        return text.split()[0]
    except IndexError:
        return ""
