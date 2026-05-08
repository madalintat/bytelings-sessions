"""Rung 3: Guided — solved version.

`make_display_name` chains several str methods in sequence:
  1. strip() — remove outer whitespace.
  2. Early exit if empty -> "(anonymous)".
  3. split() + capitalize() on each word — handles multiple spaces
     between words because split() with no arg collapses any whitespace.
  4. " ".join(...) — reassemble with single spaces.
  5. Truncation: if len(result) > max_len, take result[:max_len-1],
     rstrip() to remove any trailing space from mid-word cut, then
     append the ellipsis character "…" (one Unicode char, not "...").

The rstrip before appending "…" handles cases like "Alpha Bravo Ch "
where the cut lands on a space — rstrip drops it before the ellipsis.
"""


def make_display_name(raw: str, max_len: int = 20) -> str:
    """Turn a raw user input into a tidy display name.

    >>> make_display_name("  alice   wonderland ")
    'Alice Wonderland'
    >>> make_display_name("")
    '(anonymous)'
    >>> make_display_name("   ")
    '(anonymous)'
    >>> make_display_name("alpha bravo charlie delta", max_len=15)
    'Alpha Bravo Ch…'
    """
    stripped = raw.strip()
    if not stripped:
        return "(anonymous)"
    result = " ".join(word.capitalize() for word in stripped.split())
    if len(result) > max_len:
        result = result[: max_len - 1].rstrip() + "…"
    return result
