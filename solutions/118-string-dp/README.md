---
day: day-118-string-dp
phase: phase-5-algorithms
module: module-24-dp-greedy-backtracking
style: detective
---
# Day 118 — Why is "is this a valid word?" so slow?

A spell-check colleague pings you. Their function decides whether a
string can be split into a sequence of dictionary words. It works
fine on test inputs but **hangs** on `s = "aaaaaaaaaaaaaaaaab"` with
dictionary `["a", "aa", "aaa", "aaaa"]`.

```python
def can_segment(s, words):
    if not s:
        return True
    for w in words:
        if s.startswith(w):
            if can_segment(s[len(w):], words):
                return True
    return False
```

Looks reasonable. Why does it hang?

## The crime scene

Trace `can_segment("aaaab", ["a","aa"])` by hand:

```text
"aaaab"
  try "a"  → "aaab"
    try "a"  → "aab"
      try "a"  → "ab" → no word starts with "ab" → False
      try "aa" → "b"  → False
    try "aa" → "ab" → False     ← already computed!
  try "aa" → "aab"               ← already computed!
    ...
```

Every prefix is solved many times because each split point is reached
via many decision paths. With "a","aa","aaa","aaaa" all valid, the
branching factor is 4 at every step. 17 a's deep, you get 4^17 ≈
17 billion calls.

This is **string DP** in disguise — the subproblems are "is the
suffix starting at index i segmentable?" and they overlap. Solution:
memoize on the *position*, not the substring (avoids string slicing
overhead too).

## Suspect 1: the slicing

`s[len(w):]` creates a new string each call. That's wasteful, but
not exponentially so. Crossed off.

## Suspect 2: no memoization (the actual culprit)

```python
from functools import cache

def can_segment(s, words):
    words = set(words)
    max_len = max(map(len, words), default=0)

    @cache
    def from_index(i):
        if i == len(s):
            return True
        for L in range(1, min(max_len, len(s) - i) + 1):
            if s[i:i + L] in words and from_index(i + L):
                return True
        return False

    return from_index(0)
```

Now there are at most `len(s)` unique calls. Total work: O(len(s) ×
max_word_len). The 17-a's-deep input now finishes in microseconds.

The fix has three parts: (1) parameterize on the index, not the
suffix string; (2) memoize that helper; (3) use a set + max-length
to bound the inner loop.

## The lesson: most string DP is "1D DP indexed by position"

When the problem is "can I do X to this string?" or "minimum
operations to transform this string?" or "how many ways to parse
this string?" — the natural state is a **position** (or two, for
two-string problems).

```python
@cache
def f(i):
    if i == len(s):
        return base_case_answer
    # decide what to do starting at index i
    # combine with f(i + L) for various L
    return combined
```

This is the most common shape of string DP in the wild.

## Other classic string-DP detectives

**Palindrome partitioning.** "Min cuts to partition s into all-
palindrome pieces?" State: dp[i] = min cuts needed for `s[i:]`.
Inner loop: try every L such that `s[i:i+L]` is a palindrome.

**Regex matching with `*`.** State: dp[i][j] = "does pattern `p[:j]`
match string `s[:i]`?" Recurrence handles the wildcard explicitly.
This is the engine inside grep.

**Decode ways.** "How many ways can `'12'` decode as letters
(A=1..Z=26)?" State: dp[i] = ways to decode the suffix starting at i.

In each case, the trap is the same: write the recursion naively,
watch it explode, then add `@cache` and parameterize by index.

## WHEN to suspect string DP

The recipe: when the problem mentions splitting / matching /
transforming a string AND the recursion in your head would re-visit
the same prefix or suffix — that's overlap, that's DP.

If the recursion is tree-shaped without re-visits (parsing JSON,
walking an AST), it's not DP — it's just recursion.

## Now: open `02_fluency.py`

Same hangs-on-input bug. Add memoization.
