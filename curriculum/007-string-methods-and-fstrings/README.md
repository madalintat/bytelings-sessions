---
day: day-007-string-methods-and-fstrings
phase: phase-1-python-core
module: module-02-strings-deep
style: tour
---
# Day 7 — A guided tour of one tiny function

A teammate wrote this helper. You're reviewing it. Read every line and
notice what each method does. The function takes a raw user input and
turns it into a "display name."

```python
def make_display_name(raw: str, *, max_len: int = 20) -> str:
    cleaned = raw.strip()                        # 1
    if not cleaned:                              # 2
        return "(anonymous)"
    parts = cleaned.split()                      # 3
    name = " ".join(p.capitalize() for p in parts)  # 4
    if len(name) > max_len:                      # 5
        name = name[: max_len - 1].rstrip() + "…"
    return f"{name} ({len(parts)} word{'s' if len(parts) != 1 else ''})"  # 6
```

A line-by-line tour:

1. `.strip()` removes leading/trailing whitespace. It does **not**
   modify `raw`; strings are immutable. It returns a new string.
2. `if not cleaned:` is the truthiness check from Day 3 — empty string
   is falsy.
3. `.split()` with no args splits on **any** run of whitespace (spaces,
   tabs, newlines collapse to one separator). Returns a `list[str]`.
4. A generator expression inside `" ".join(...)`. `.capitalize()`
   uppercases the first letter and lowercases the rest of each word.
   `join` glues them with spaces.
5. If the joined name is too long, slice it (Day 6) and tack on `…`.
   `.rstrip()` cleans up the case where the slice ends mid-word with
   a trailing space.
6. An **f-string** with two embeddings: `{name}` interpolates the
   variable, and `{len(parts)}` calls a function inline. The trailing
   conditional handles English plural agreement.

## What an f-string actually is

`f"x={x}"` is shorthand for "build a string by inserting the value of
`x`." The `f` prefix flips the brackets from literal `{}` into
expression slots. You can put any Python expression inside.

```python
price = 9.5
qty = 3
msg = f"{qty} items at ${price:.2f} = ${qty * price:.2f}"
# "3 items at $9.50 = $28.50"
```

The `:.2f` is a **format spec**: "float, 2 decimals." The most useful
ones to remember:

| Spec | Effect |
|---|---|
| `:.2f` | 2 decimal places |
| `:,` | thousands separator |
| `:>10` | right-align in 10 chars |
| `:<10` | left-align in 10 chars |
| `:0>3` | pad with zeros to 3 chars |
| `:%` | percentage |

## Methods worth memorizing today

`.strip()`, `.lstrip()`, `.rstrip()`, `.lower()`, `.upper()`,
`.startswith()`, `.endswith()`, `.replace(old, new)`, `.split(sep)`,
`.join(iter)`, `.find(sub)` (returns `-1` if missing), `.count(sub)`.
You'll use these *every day*.

## Now: open `02_fluency.py`

Three small string-method calls are wrong. Patch them.
