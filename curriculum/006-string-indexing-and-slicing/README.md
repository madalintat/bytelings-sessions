---
day: day-006-string-indexing-and-slicing
phase: phase-1-python-core
module: module-02-strings-deep
style: trace
---
# Day 6 — Predict each line

You're reading code in a PR review. Five string-slicing lines appear.
You need to call out what each one returns *without running it*. Walk
the trace below, line by line, and predict before you scroll.

```python
s = "panopticon"
#    0123456789
#   -0987654321  (negative indices, -0 is just 0)

a = s[0]      # ?
b = s[-1]     # ?
c = s[2:6]    # ?
d = s[:3]     # ?
e = s[-4:]    # ?
f = s[::2]    # ?
g = s[::-1]   # ?
```

Decide your answers, then check:

- `a` → `"p"`. Index 0 is the first char.
- `b` → `"n"`. Negative indices count from the end.
- `c` → `"opti"`. Slice is `[start:stop)`, stop exclusive.
- `d` → `"pan"`. Missing start means 0.
- `e` → `"icon"`. Missing stop means "to the end".
- `f` → `"pnpio"`. Step 2 means "every other char".
- `g` → `"nocitponap"`. Step `-1` reverses.

## The shape of a slice

`s[start:stop:step]`. All three are optional. Defaults:

- `start` defaults to `0` (or `len(s)-1` if `step` is negative).
- `stop` defaults to `len(s)` (or `-len(s)-1` if `step` is negative).
- `step` defaults to `1`.

The half-open interval `[start, stop)` is the same convention as
`range()`. It's chosen so `s[:k] + s[k:] == s` for any `k`.

## One more trace, edge cases this time

```python
s = "hello"
s[10:20]    # ""        — out of range slices DON'T raise; they return ""
s[10]       # IndexError — but indexing does
s[-100:2]   # "he"      — negative start clamps to 0
s[2:1]      # ""        — start >= stop with positive step → empty
```

Strings are **immutable**, so every slice produces a *new* string. You
can't do `s[0] = "H"` — Python will raise `TypeError`. (Day 8 leans on
this fact.)

## Two short rules

1. When in doubt, write `s[i:j]` and read it as "from `i`, up to but
   not including `j`."
2. Negative `step` is a reverse iterator. `s[::-1]` is the canonical
   "reverse a string" idiom.

## Now: open `fluency.py`

Three slice expressions are wrong. Read each test, predict the right
slice, then patch it.
