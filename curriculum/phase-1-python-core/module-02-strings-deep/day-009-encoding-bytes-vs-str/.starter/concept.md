---
day: day-009-encoding-bytes-vs-str
phase: phase-1-python-core
module: module-02-strings-deep
style: detective
---
# Day 9 — The mystery of the missing emoji

A teammate's script reads a file of customer reviews and counts how
many contain the heart emoji `♥`. It works on her laptop. On the prod
server it crashes:

```text
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position
27: invalid continuation byte
```

You take the case. You have three suspects.

## Suspect 1: the file is not UTF-8

`str` in Python is a sequence of Unicode **code points** — abstract
characters. `bytes` is a sequence of raw 8-bit values. Files on disk
hold bytes. When you call `open(path)` (text mode), Python *decodes*
those bytes into a `str` using a default encoding. On Linux/macOS
that's usually UTF-8. On Windows it can be `cp1252`.

If the file was written as Latin-1 and you read it as UTF-8, certain
byte sequences are invalid. Bang. UnicodeDecodeError.

```python
# The fix: state the encoding explicitly. Don't trust the default.
with open(path, encoding="utf-8") as f:
    text = f.read()
```

## Suspect 2: an unread byte-order mark (BOM)

Some Windows tools (Notepad, Excel) prepend a BOM (`﻿`) to
"mark" the file as UTF-8. Read with `encoding="utf-8"` and the BOM
shows up as a literal first character. Read with `encoding="utf-8-sig"`
and Python strips it.

## Suspect 3: bytes vs str confusion at the boundary

```python
b = "café".encode("utf-8")   # b'caf\xc3\xa9'  — bytes (4 chars → 5 bytes)
s = b.decode("utf-8")        # 'café'          — back to str

len("café")            # 4   (code points)
len("café".encode())   # 5   (UTF-8 bytes)
```

The pattern: **decode at the input boundary, encode at the output
boundary, and use `str` everywhere in between.** Mixing `bytes` and
`str` in the middle leads to `TypeError: a bytes-like object is
required, not 'str'` (or vice versa).

| You have | You want | Use |
|---|---|---|
| `str` | `bytes` | `s.encode("utf-8")` |
| `bytes` | `str` | `b.decode("utf-8")` |
| `bytes` you don't know the encoding of | best-effort `str` | `b.decode("utf-8", errors="replace")` |

`errors="replace"` swaps undecodable bytes for `�` (the "replacement
character", a black diamond with a `?`). Better than crashing in a log
line; worse than knowing the right encoding.

## Verdict

Almost always it's Suspect 1: a file is in some other encoding. The
fix is to *know* and *state* the encoding when you open the file. The
worst Python encoding bugs come from the silent default that "happens
to work" in dev and breaks in prod.

## Now: open `02_fluency.py`

Three encode/decode lines are wrong. The detective's case file (the
tests) tells you the expected output for each.
