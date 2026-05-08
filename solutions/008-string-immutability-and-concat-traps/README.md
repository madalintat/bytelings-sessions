---
day: day-008-string-immutability-and-concat-traps
phase: phase-1-python-core
module: module-02-strings-deep
style: pain
---
# Day 8 — Why your loop is slow

You wrote a function that builds a 100,000-character string from a list
of words. It works. But it takes 4 seconds. The user complains. You
profile it. The hot line is one you trusted:

```python
def join_words_slow(words):
    out = ""
    for w in words:
        out += w + " "      # the trap
    return out.rstrip()
```

## What's actually happening

Strings are **immutable**. `out += w + " "` does not modify `out` —
Python can't, the underlying memory is frozen. Instead, it:

1. Allocates a new buffer big enough for `out + w + " "`.
2. Copies the entire old `out` into it.
3. Copies `w` and `" "` after.
4. Throws away the old `out`.

For `n` words you copy `1 + 2 + 3 + ... + n` characters. That's
**O(n²)** time. With 100,000 words, you're doing ~5 billion char-copies
to produce a 100k-char string. Python may optimize some cases via
in-place buffer reuse, but you cannot rely on it.

## The fix: build a list, then `join`

```python
def join_words_fast(words):
    parts = []
    for w in words:
        parts.append(w)
    return " ".join(parts)
```

`list.append` is amortized O(1), so the loop is O(n). `" ".join()`
walks the list once and pre-computes the final size — also O(n). Total
O(n). On 100k words this drops from seconds to milliseconds.

The pythonic one-liner: `" ".join(words)` directly. No loop needed.

## What "immutable" means in practice

```python
s = "hello"
s[0] = "H"        # TypeError: 'str' object does not support item assignment
s = "Hello"       # this is FINE — you're rebinding the name `s`
                  # to a new object. The old "hello" is unchanged.
```

Two rules to internalize:

1. **No string method modifies the original.** Every method returns a
   new string. `s.upper()` does not change `s`. You must reassign:
   `s = s.upper()`.
2. **`+=` on a string in a loop is a code smell.** It's not always
   slow, but you can't tell at the call site. Use `"".join(...)` (or
   `io.StringIO` for very complex builders) instead.

## A bonus pain point: `+` for many strings

```python
greeting = "Hello, " + first + " " + last + "!"   # fine for 4-5 pieces
greeting = f"Hello, {first} {last}!"              # better; readable
```

For a fixed number of pieces, `+` and f-strings are equally fast.
The pain only arrives when the count grows in a loop.

## Now: open `fluency.py`

Two of these functions look reasonable but suffer the trap. Fix them.
