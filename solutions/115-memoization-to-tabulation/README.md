---
day: 115-coin-change-greedy-fails
phase: phase-5-algorithms
module: module-24-dp-greedy-backtracking
style: detective
---
# Day 115 — Coin change: greedy looks right and is wrong

You learned the three lenses on Day 114. Today's job is to prove —
on a problem you'd swear is greedy — that *greedy is the wrong
lens*. The wrongness lands faster than any textbook explanation.

## The problem

```
Given a list of coin denominations (positive ints) and a target amount,
return the MINIMUM number of coins that sum to target. Each coin can
be used unlimited times. If target can't be made, return -1.
```

US coins (`[1, 5, 10, 25]`, target 30) → easy: a quarter and a nickel,
2 coins. Greedy works: take the largest coin that doesn't overshoot,
repeat.

## The trap

Now try `[1, 4, 5]` with target `8`.

Greedy says: take 5 (largest ≤ 8), now we need 3, take 1, take 1, take 1.
That's **4 coins**: `[5, 1, 1, 1]`.

But the right answer is **2 coins**: `[4, 4]`.

Greedy was wrong. Not by an off-by-one — by a factor of 2. And there
was no way to *patch* the greedy algorithm to detect this case at
the moment of choosing. Once you took the 5, the remaining 3 had no
better option; the mistake was upstream.

This is the deep lesson Day 114 promised: **greedy correctness is a
proof obligation, not an instinct.** When the proof doesn't go
through, you fall through to the next lens.

## Why it falls through to DP

Re-read the problem with DP eyes:

```
min_coins(target) = 1 + min(min_coins(target - c) for c in coins
                              if target - c >= 0)
```

`min_coins(8)` with coins `[1, 4, 5]`:
- try 1: `1 + min_coins(7)` — needs to recurse
- try 4: `1 + min_coins(4)` — needs to recurse
- try 5: `1 + min_coins(3)` — needs to recurse

Now trace `min_coins(7)`:
- try 1: `1 + min_coins(6)` — needs `min_coins(6)`
- try 4: `1 + min_coins(3)` — **same min_coins(3) we just saw**
- try 5: `1 + min_coins(2)`

The same subproblem (`min_coins(3)`) shows up under two different
parents. Trace deeper and `min_coins(2)`, `min_coins(1)`, `min_coins(0)`
get hit dozens of times across branches. **Subproblems overlap →
DP.**

## The DP solution

```python
def min_coins(coins: list[int], target: int) -> int:
    INF = float("inf")
    dp = [INF] * (target + 1)
    dp[0] = 0
    for t in range(1, target + 1):
        for c in coins:
            if t - c >= 0 and dp[t - c] + 1 < dp[t]:
                dp[t] = dp[t - c] + 1
    return dp[target] if dp[target] != INF else -1
```

`dp[t]` is the minimum coins for amount `t`. Each `t` is computed
exactly once. O(target × len(coins)) time, O(target) space. For
`coins=[1,4,5], target=8`: `dp = [0,1,2,3,1,1,2,3,2]`. Answer: 2.

## What today exercises

- **Recognize when greedy is provably wrong.** The fluency drill
  shows you 4 coin sets; you say which support greedy and which
  don't. The diagnose helper points at the failure case for the
  wrong answers.
- **Write the DP recurrence**, then the iterative tabulation
  (rung 3 + 4).
- **Apply** (rung 5): given an arbitrary coin set, output BOTH the
  greedy answer and the DP answer side by side. Watch the gap close
  to zero on US coins, open up on adversarial sets. The visual
  proof is the lesson.

## Pattern Catalog

`bytelings patterns P-28` — memoize-recursive. The top-down DP form
of today's solution. The iterative `dp` array is the bottom-up
form (called *tabulation*).

## Why this lens, not greedy

For greedy to be correct on coin change, the coin set must satisfy
the *matroid* property — every "remove the largest, recurse" path
is optimal. US coins satisfy it. `[1, 4, 5]` doesn't: removing 5
from 8 leaves 3, but the optimal solution doesn't include 5 at all.
Without that algebraic property, greedy has no anchor.

You won't memorize "matroid." You'll memorize: **whenever a problem
asks for an optimum AND the input includes adversarially-chosen
parameters, distrust greedy.** Try DP first.

## Now: open `fluency.py`

Five coin-set problems. For each, mark "greedy" or "needs DP" and
the diagnostic will tell you which assumption broke.
