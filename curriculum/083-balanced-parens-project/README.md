---
day: 083-balanced-parens-project
phase: phase-4-data-structures
module: module-16-stacks-queues-deques
style: story
---
# Day 83 — A linter from a stack

It's a Friday. The intern committed 800 lines of templated SQL with a
single missing `)` somewhere in the middle. CI is red. Everyone is
guessing line numbers. You think: *I bet I could write a one-page
script that finds the unbalanced bracket exactly.*

You can. And the data structure that makes it trivial is the stack
you built on Day 80.

## The trick

Walk the text once, left to right.

- Hit an opener (`(`, `[`, `{`) — push it on a stack.
- Hit a closer (`)`, `]`, `}`) — pop the top.
  - If the stack was empty, you've got a stray closer (no opener to
    match).
  - If the popped opener doesn't match the closer (e.g. you pushed
    `(` and now see `]`), you've got a mismatched pair.
- After walking the whole string, if the stack is non-empty, you've
  got an unclosed opener.

That's it. The stack remembers exactly which opener is "currently
hungry" for a closer. The most recently opened bracket must close
first — which is precisely LIFO. The data structure fits the problem
shape; you barely have to think.

## Why this is the canonical stack example

Every textbook uses balanced-parentheses as the introductory stack
problem because the matching rule (newest open closes first) and the
LIFO rule are the same rule. If you understand one, you understand the
other. You're not just solving a homework problem — you're seeing the
*reason stacks exist* in pure form.

This is also the seed of a real compiler: every parser stacks
something. Function call frames are a stack. Expression evaluation is
a stack. Today's tiny script is the same algorithm a real linter runs,
just with more bracket types and better error messages.

## The micro-tour

```python
def is_balanced(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack
```

Six lines. One pass. O(n) time, O(n) worst-case space.

## What you'll build

Today's project chunk goes one step further: not just a yes/no, but a
**precise error report**: which character index is wrong, and what
would have made it right. Real linters do this. You'll do it too,
and the data structure does most of the work.

## Now: open `fluency.py`

Two near-correct balanced-paren attempts, each with one bug.
