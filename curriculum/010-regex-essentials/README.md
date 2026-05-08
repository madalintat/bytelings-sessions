---
day: 010-regex-essentials
phase: phase-1-python-core
module: module-02-strings-deep
style: build-it
---
# Day 10 — Pretend Python doesn't have `re`

Suppose you have to write a "find all phone-number-shaped strings"
function. No regex library allowed. You'd write a state machine: walk
each char, track "did I see 3 digits, then a dash, then 4 digits…",
backtrack on mismatch. It works, but it's 80 lines and brittle.

That state machine is exactly what `re` compiles for you, in C, from
a tiny declarative pattern. Once you see it that way, the syntax stops
feeling magical.

## A small worked example

```python
import re

text = "Call 555-1212 or 312-555-9876, please."
pattern = r"\d{3}-\d{4}"
matches = re.findall(pattern, text)
# ['555-1212', '555-9876']
```

Read the pattern as: "three digits, a dash, four digits." Each piece:

- `\d` — a digit (0–9). One char.
- `{3}` — repeat the previous thing exactly 3 times.
- `-` — a literal dash.

The `r"..."` is a **raw string**: backslashes aren't interpreted by
Python, so `\d` reaches `re` intact. Always use raw strings for
patterns. Always.

## The 12 building blocks

| Atom | Means | Example match |
|---|---|---|
| `.` | any one char (except newline) | `a` in `a` |
| `\d` `\w` `\s` | digit, word-char, whitespace | `5`, `a`, ` ` |
| `\D` `\W` `\S` | the negations | non-digit, etc. |
| `[abc]` | one of a, b, or c | `a` |
| `[^abc]` | any char EXCEPT a, b, c | `x` |
| `[a-z]` | range | any lowercase letter |
| `^` `$` | start / end of string (or line) | anchors |
| `\b` | word boundary | between `\w` and non-`\w` |
| `*` | 0 or more | `a*` matches `""` or `aaaa` |
| `+` | 1 or more | `a+` requires at least one |
| `?` | 0 or 1 (optional) | `colou?r` matches both spellings |
| `{n,m}` | between n and m repeats | `\d{2,4}` |
| `(...)` | capture group | groups[0] = whole, groups[1] = inner |
| `(?:...)` | non-capturing group | grouping without a slot |

## Functions you'll use

```python
re.findall(pat, s)    # list of all matches (or tuples if groups)
re.search(pat, s)     # first match anywhere — Match obj or None
re.match(pat, s)      # match at START only — easy to forget
re.fullmatch(pat, s)  # must match the whole string
re.sub(pat, repl, s)  # replace
re.split(pat, s)      # split by pattern
```

A `Match` object: `.group(0)` is the whole match; `.group(1)` is the
first capture group; `.groups()` is a tuple of all groups.

## A tiny gotcha

`re.search("hello", s)` finds `"hello"` anywhere. `re.match("hello", s)`
only matches if `s` starts with `hello`. New users reach for `match`
because the name is friendly; almost always they wanted `search` or
`fullmatch`.

## Now: open `fluency.py`

Three patterns are slightly off. Read each test, find the bug, fix
the pattern.
