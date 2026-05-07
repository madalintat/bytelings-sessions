---
day: day-099-base-and-recursive-cases
phase: phase-5-algorithms
module: module-20-recursion
style: metaphor
---
# Day 99 — Russian dolls and the smallest doll

You're holding a matryoshka — a Russian nesting doll. To "process" the
whole stack, you have one rule: open the doll in your hand, and apply
the same rule to whatever's inside. You stop when you find a tiny
solid doll that doesn't open.

That's recursion. Two parts, no exceptions:

1. **The base case** — the tiniest doll. The thing so small you can
   answer it directly without opening anything.
2. **The recursive case** — every other doll. You don't solve it; you
   just shrink the problem by one step and pass it down.

Forget anything you've heard about "a function that calls itself." That
description is technically right and pedagogically useless. The real
question every recursive function answers is: *what's the smallest
version of this problem, and how do I shrink any bigger version toward
it?*

## Sum of a list, the matryoshka way

```python
def total(nums):
    if not nums:           # smallest doll: empty list, total is 0
        return 0
    return nums[0] + total(nums[1:])   # bigger doll: peel one off
```

Read it as: "the total of an empty list is 0. The total of any other
list is its first item plus the total of the rest." Two sentences.

## WHEN you reach for recursion

Recursion is the right tool when the problem is **self-similar** — a
big version of it contains smaller versions of itself. Examples you
will actually hit:

- Walking a directory tree (each folder contains files *and folders*).
- Parsing JSON (a value can be a list of *values*).
- Evaluating expressions (`(2 + (3 * 4))` — parens inside parens).
- Anything tree-shaped: HTML, ASTs, comment threads, org charts.

If the problem isn't self-similar, recursion is overkill. A flat list
of numbers? A `for` loop is clearer.

## The two failure modes

- **Forgot the base case** → infinite recursion → `RecursionError`.
- **Recursive case doesn't shrink** → also infinite recursion. If
  `total(nums)` calls `total(nums)` instead of `total(nums[1:])`,
  you've built a forever loop with extra steps.

When you're stuck designing a recursive function, write the base case
first. Always. Then ask: "given the answer for one-size-smaller, how
do I build the answer for this size?" That's the whole job.

## Now: open `02_fluency.py`

Two recursive functions, each missing exactly one thing — the part
that stops them. Find it. Make them stop.
