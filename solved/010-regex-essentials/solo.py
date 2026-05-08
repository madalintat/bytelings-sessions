"""Rung 4: Solo — solved version.

`find_emails` uses a single compiled regex that matches the local part
and domain according to the spec:
  - Local part: `[\\w.+%-]+` — word chars, dots, plus signs, hyphens, underscores.
  - `@`
  - Domain: one or more labels separated by dots, final label >= 2 letters.
    `[\\w-]+` per label (alphanumeric + hyphens), ending with `\\.[a-zA-Z]{2,}`.

The regex is case-insensitive via `re.IGNORECASE`, and all matches are
lowercased before returning.

Key design choice: `re.findall` with a pattern that doesn't anchor to
word boundaries lets the regex engine find all non-overlapping matches.
Because the local-part excludes `@`, there's no risk of one match
consuming the `@` needed by the next.
"""
import re

_EMAIL_RE = re.compile(
    r"[a-zA-Z0-9_.+%-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}"
)


def find_emails(text: str) -> list[str]:
    return [m.lower() for m in _EMAIL_RE.findall(text)]
