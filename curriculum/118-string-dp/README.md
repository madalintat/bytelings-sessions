---
day: 118-word-break-bridge
phase: phase-5-algorithms
module: module-24-dp-greedy-backtracking
style: detective
---
# Day 118 — Word break: where backtracking and DP meet

Days 116 and 117 cleanly separated the lenses: DP for compact-state
optimization, backtracking for tree-shaped search. Today's problem
sits on the bridge — both lenses fit, and seeing why is the
graduation moment.

## The problem

```
Given a string `s` and a list `words`, return True iff `s` can be
segmented into a sequence of words from the list. Words can be
reused.
```

Example: `s = "leetcode"`, `words = ["leet", "code"]` → True.
`s = "applepenapple"`, `words = ["apple", "pen"]` → True.
`s = "catsandog"`, `words = ["cats", "dog", "sand", "and", "cat"]` → False.

## First instinct: backtracking

The shape *is* a tree of choices. At position `i` in `s`, try every
word that matches starting at `i`; if it does, recurse from `i +
len(word)`. If you reach `i == len(s)`, success.

```python
def can_break(s: str, words: list[str]) -> bool:
    word_set = set(words)
    def solve(i: int) -> bool:
        if i == len(s):
            return True
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in word_set and solve(j):
                return True
        return False
    return solve(0)
```

This works. For small inputs it's fast. For adversarial inputs like
`s = "aaaaaaaaaaaab"`, `words = ["a", "aa", "aaa", "aaaa", "aaaaa"]`,
**it's exponential**. Each position has many word choices, and
backtracking explores them all from the same starting point
repeatedly. There's a fix screaming for attention.

## Second look: DP via memoization

Notice: `solve(j)` is called with the same `j` from many different
call sites. That's the DP signal. Cache it:

```python
from functools import cache

def can_break(s: str, words: list[str]) -> bool:
    word_set = set(words)
    @cache
    def solve(i: int) -> bool:
        if i == len(s):
            return True
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in word_set and solve(j):
                return True
        return False
    return solve(0)
```

One decorator. The exponential blow-up collapses to **O(n²)**:
each position visited once, each call does O(n) work scanning ahead.

This is the bridge. The *control flow* is still backtracking (try a
choice, recurse, return on success). The *correctness optimization*
is DP (cache the results). One concept rarely shows up without the
other in real problems.

## The bottom-up DP version (for completeness)

```python
def can_break(s: str, words: list[str]) -> bool:
    word_set = set(words)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]
```

`dp[i]` = True iff `s[:i]` can be segmented. Same O(n²) complexity,
no recursion. Pick this when you want the iterative shape; pick the
memoized recursion when the recurrence is more readable that way
(usually true for tree-of-choices problems).

## Today's exercises

- **Fluency**: trace the memoized version on a tiny adversarial
  input. The diagnose helper catches "you forgot @cache" by checking
  call counts.
- **Guided**: fill in the `for j in range(i + 1, len(s) + 1)` body.
- **Solo**: extend to *return the segmentation*, not just True/False.
  Hint: store the chosen word per position in a parallel array.
- **Apply**: a CLI that reads a sentence with no spaces and a
  dictionary file, prints the most likely segmentation. (Optional:
  stretch to the *all-segmentations* version which is always
  exponential — there's no escaping the output size.)

## Pattern Catalog

`bytelings patterns P-28` — memoize-recursive. Today is its
canonical use: a recursion that's exponential without caching and
polynomial with it. The decorator IS the algorithmic improvement.

## When you see this pattern in the wild

Word break, regex matching, string splitting under constraints —
all bridge problems. The recipe: write the recursion as if it's a
plain backtracking search; if you hit the same subproblem multiple
times, slap `@cache` on. If complexity drops from exponential to
polynomial, you've found a DP problem dressed as a search problem.

## Now: open `fluency.py`
