"""Rung 4: Solo — solved version.

`english_list` uses a single conditional chain over the list length:
  - 0 items  -> ""
  - 1 item   -> names[0]
  - 2 items  -> "a and b"
  - 3+ items -> join all but last with ", ", add ", and " before the last.

The join-then-append pattern is O(n) — it never uses += in a loop.
For 3+ items:
    ", ".join(names[:-1]) + ", and " + names[-1]
produces the Oxford comma naturally.

Two-item case is handled separately because `", ".join(["a"]) + ", and b"`
would add an Oxford comma that English convention omits for two items.
"""


def english_list(names: list[str]) -> str:
    if not names:
        return ""
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return ", ".join(names[:-1]) + ", and " + names[-1]
