---
day: 066-property-based-testing-intro
phase: phase-3-quality-production
module: module-12-testing-with-pytest
style: metaphor
---
# Day 66 — A pop quiz versus a thousand quizzes

Imagine you're hiring a translator. You give them one sentence in
English, ask for the French. They get it right. Hired?

Of course not. One sentence proves nothing. You'd give them a
hundred sentences. You'd give them tricky ones. You'd give them
empty strings, and emoji, and the kind of stuff your real users will
type at 3 AM.

Example-based tests — `assert encode("hello") == "olleh"` — are the
one-sentence interview. **Property-based tests are the thousand-
question interview**, and you don't have to write the thousand
questions. You write the *rules* the answers must obey. The library
generates the questions for you.

## What's a "property"?

A property is a statement about your function that should be true
for *any* valid input. Two classics:

1. **Round-trip:** `decode(encode(x)) == x`. If you've got an
   `encode` and a `decode`, this property is free testing-gold.
2. **Invariant:** `len(sorted(xs)) == len(xs)`. Sorting can't change
   length, regardless of the input.

You write a property as a function that takes the generated input and
asserts. The library hands you thousands of inputs and reports the
first one that breaks the property — *minimized*. (If a 1000-element
list breaks your sort, hypothesis won't show you the 1000-element list.
It'll shrink it to the smallest list that still fails. That's gold.)

## Hypothesis, the library

```python
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_sort_preserves_length(xs):
    assert len(sorted(xs)) == len(xs)

@given(st.text())
def test_encode_decode_roundtrip(s):
    assert decode(encode(s)) == s
```

`given` decorates a normal pytest function. `strategies` are
generators: `st.integers()`, `st.text()`, `st.lists(st.floats())`,
`st.dictionaries(...)`, and many more. Hypothesis runs the function
many times with generated inputs (~100 by default), and on failure,
**shrinks** the failing input to a minimal reproducer.

## Properties you'll learn to spot

| Pattern | Example |
|---|---|
| Round-trip | `parse(format(x)) == x`, `decompress(compress(x)) == x` |
| Invariant | `len`, `sum`, `set` of input vs output |
| Idempotence | `f(f(x)) == f(x)` (e.g., `slugify(slugify(x)) == slugify(x)`) |
| Symmetry | `add(a, b) == add(b, a)` |
| Oracle | `your_fast_thing(x) == known_slow_thing(x)` for many `x` |

A function with no obvious properties usually has at least one *bound*:
"the result is between 0 and len(input)" — try that.

## Why this isn't every test

Properties find *classes* of bugs. They're terrible at proving "for
the input `(3, 4)` we return exactly `7`." That's what example-based
tests still do best. Use both: a small set of tight examples for the
specific contract, plus a property test or two to catch the surprises
you didn't think of (empty strings, nulls, huge numbers, unicode).

## Now: open `fluency.py`

Two property tests are written but the function has a subtle bug.
Run them, watch hypothesis shrink the input to a tiny counter-example,
fix the bug.
