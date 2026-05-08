"""Rung 4: Solo — solved version.

`flip_name` handles the "Last, First" -> "First Last" transformation:
  1. Strip outer whitespace first to handle leading/trailing spaces.
  2. Empty / whitespace-only -> return "".
  3. If a comma is present, split on the FIRST comma (partition handles
     this cleanly), strip each part, capitalize each word of each part,
     then join as "first last".
  4. If no comma, just capitalize each word of the whole thing.

Using str.split() + capitalize() on each token handles multi-word
names like "DOE" -> "Doe" because capitalize() lowercases everything
after the first char.

`partition` is preferred over `split(',', 1)` because it always
returns a 3-tuple (before, sep, after), avoiding edge-case indexing.
"""


def flip_name(s: str) -> str:
    s = s.strip()
    if not s:
        return ""
    if "," in s:
        last, _, first = s.partition(",")
        last = " ".join(w.capitalize() for w in last.split())
        first = " ".join(w.capitalize() for w in first.split())
        return f"{first} {last}".strip()
    return " ".join(w.capitalize() for w in s.split())
