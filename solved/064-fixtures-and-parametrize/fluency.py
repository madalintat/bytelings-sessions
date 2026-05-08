"""Rung 2: Fluency drill — solved version.

The slugify function is correct as given. The fluency task was to
replace five copy-pasted tests in the test file with one parametrized
test. This file is unchanged.
"""


def slugify(text: str) -> str:
    """Lowercase, replace runs of non-alphanumerics with single dashes,
    strip leading/trailing dashes."""
    out = []
    prev_dash = True  # treat start-of-string like a leading dash
    for ch in text.lower():
        if ch.isalnum():
            out.append(ch)
            prev_dash = False
        elif not prev_dash:
            out.append("-")
            prev_dash = True
    s = "".join(out)
    return s.rstrip("-")
