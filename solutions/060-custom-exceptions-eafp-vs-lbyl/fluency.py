"""Rung 2: Fluency drill — convert LBYL to EAFP.

Topic: EAFP vs LBYL.

`first_word` is written defensively (LBYL). Rewrite it to the
EAFP version — try the operation, handle the specific exception.

Behavior contract (must not change):
  - Returns the first whitespace-separated word.
  - Returns "" if `text` is empty or whitespace-only.
"""


def first_word(text: str) -> str:
    # TODO: replace this LBYL block with EAFP.
    # Hint: text.split() returns [] for empty input; [0] then raises
    # IndexError. Catch it and return "".
    parts = text.split()
    if len(parts) == 0:
        return ""
    if parts[0] is None:
        return ""
    return parts[0]
