---
day: day-119-greedy-intuition-and-failures
phase: phase-5-algorithms
module: module-24-dp-greedy-backtracking
style: compare
---
# Day 119 — When "always grab the biggest" works (and when it doesn't)

You're at a vending machine making change. You have coins {25, 10,
5, 1}. Need to give 30 cents. The greedy algorithm says: always grab
the biggest coin that fits.

```text
30 → grab 25, 5 left
 5 → grab 5,  0 left
done. 2 coins.
```

Optimal. Greedy is right.

Now you're in a fictional country with coins {1, 4, 6}. Need 9 cents.

```text
Greedy:        Optimal:
9 → grab 6     9 = 4 + 4 + 1?  no, that's 3 coins
3 → 1+1+1      9 = 6 + ... 6+1+1+1 also 4 coins
total: 4       so let me check: 9 = 4 + 4 + 1 = 3 coins ← best
```

Wait — the optimal is 3 (4+4+1), greedy gives 4 (6+1+1+1). Greedy
is wrong.

The two examples have the same shape. So why does greedy work for
one and fail for the other?

## Way A — Greedy

Pick the locally best option at each step. Never reconsider.

```python
def greedy_change(amount, coins):
    coins = sorted(coins, reverse=True)
    used = 0
    for c in coins:
        used += amount // c
        amount %= c
    return used if amount == 0 else -1
```

O(n log n) for the sort, O(n) after. Tiny code, tiny memory.

## Way B — DP (always-correct)

We saw this on day 114: try every choice, memoize, take the best.

```python
@cache
def min_coins(amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    return 1 + min(min_coins(amount - c) for c in coins)
```

Slow-ish (O(amount × n)) but provably correct.

## Why greedy worked on US coins and failed on {1, 4, 6}

The US coin system has a property called the **matroid** structure
(or, more loosely, "greedy-friendly"): grabbing the biggest coin
always leaves you with a sub-problem that's *also* solved best by
greedy. {1, 4, 6} doesn't have it: grabbing 6 leaves you with 3,
which can only be made as 1+1+1. Whereas if you'd skipped 6 you'd
have a better option.

There's no simple rule that tells you greedy will work. You **prove
it case by case**, or you don't trust greedy.

## When greedy DOES provably win (memorize these)

- **Activity selection.** Pick the meeting that ends earliest, then
  repeat. Provably optimal for "max non-overlapping meetings."
- **Huffman coding.** Always merge the two lowest-frequency
  symbols. Optimal prefix codes.
- **Dijkstra's algorithm.** Always extend the shortest known
  unvisited path. Optimal shortest paths on non-negative weights.
- **Minimum spanning tree** (Kruskal, Prim). Always add the cheapest
  edge that doesn't form a cycle. Optimal MST.
- **Fractional knapsack.** Pick by best value-per-weight ratio.
  Optimal *if you can take fractions*. (Integer knapsack? Greedy
  fails — needs DP.)

For everything else, your default should be: "test greedy with a
small example. If it fails, switch to DP."

## The diagnostic

When you're tempted by a greedy solution, write the smallest input
where it might fail and run it. If your "always pick the biggest"
gives a different answer than DP, greedy is wrong for this problem.
This 30-second check saves more careers than any tool I know.

## WHEN to suspect greedy

Greedy is the right tool when:

- The problem has an obvious "best next choice" with no
  counter-pull — picking it doesn't make any other future choice
  worse.
- The objective is monotone (adding more never hurts).
- You can prove (or recognize from history) that local optima
  combine to a global optimum.

Don't reach for greedy on optimization problems with constraints
that interact ("budget AND weight AND..."). DP, almost always.

## Now: open `02_fluency.py`

A greedy "max meetings" picker that sorts the wrong way. Fix it.
