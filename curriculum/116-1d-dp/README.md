---
day: day-116-1d-dp
phase: phase-5-algorithms
module: module-24-dp-greedy-backtracking
style: build-it
---
# Day 116 — Build a 1D DP from scratch

You've seen `@cache`. Now build the table by hand.

A **1D DP** is one where the state is described by one integer: a
position in an array, a length, an amount. The table is a single
list, and each entry is computed from a small fixed number of
earlier entries. Pretend Python doesn't ship `functools.cache` —
build the table directly.

## The recipe (memorize this)

Every 1D DP problem has the same skeleton:

1. **Define the state.** "Let `dp[i]` be the answer for the
   subproblem of size i / ending at index i / using the first i
   items."
2. **Write the recurrence.** "`dp[i]` is X in terms of `dp[i-1]`,
   `dp[i-2]`, ..." Write this on paper before you write code.
3. **Set the base cases.** What's `dp[0]`, `dp[1]`?
4. **Choose fill order.** Almost always left-to-right, because each
   `dp[i]` depends on smaller indices.
5. **Return `dp[n]`** (or wherever the answer lives).

Five lines on a sticky note. The art is in step 1: choosing the
state. Get that wrong and the rest collapses.

## Worked example: longest increasing subsequence (LIS)

Given `[10, 9, 2, 5, 3, 7, 101, 18]`, the longest strictly increasing
subsequence is `[2, 3, 7, 101]`, length 4.

**State:** `dp[i]` = the length of the LIS ending exactly at index i.
(Crucially: ending *at* i, not "in the first i elements." Subtle but
load-bearing.)

**Recurrence:**
```
dp[i] = 1 + max(dp[j] for j < i if arr[j] < arr[i],   default 0)
```

In words: "to end at i, look at every earlier index j whose value
is smaller; the best LIS ending at i is 1 plus the best LIS ending
at the best such j."

**Base:** `dp[0] = 1` (a single element is a length-1 sequence).

**Code:**
```python
def lis(arr):
    if not arr:
        return 0
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

O(n²). There's a clever O(n log n) version using binary search; the
recipe stays the same, only the inner loop gets smarter.

## A simpler example: max subarray sum (Kadane's algorithm)

Given `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`, the contiguous subarray with
the largest sum is `[4, -1, 2, 1]` summing to 6.

**State:** `dp[i]` = the largest sum of a subarray ending exactly
at index i.

**Recurrence:**
```
dp[i] = max(arr[i], dp[i-1] + arr[i])
```

"Either start fresh at i (sum = arr[i]) or extend the best subarray
ending at i-1." Either you keep the running tail or you reset.

```python
def kadane(arr):
    best = cur = arr[0]
    for x in arr[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
```

O(n) time, O(1) space (we rolled the table into one variable).

## WHEN you reach for 1D DP

Trigger phrases:

- "Maximum/minimum **ending at**, **using up to**, **of length N**."
- "Number of ways to reach **the i-th** something."
- "Longest/shortest **subsequence** of an array."

Real-world hits: stock-trading optimal-day problems, run-length
analytics, climbing/path-counting puzzles, basic DNA pattern length
problems, dynamic resource allocation along time.

## Now: open `fluency.py`

A bottom-up max-subarray-sum (Kadane's) with the recurrence written
backward. Fix it.
