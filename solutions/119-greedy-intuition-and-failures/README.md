---
day: 119-greedy-proof-craft
phase: phase-5-algorithms
module: module-24-dp-greedy-backtracking
style: build-it
---
# Day 119 — Greedy: a proof, not a guess

Day 115 showed greedy failing. Today it works *and you'll prove it*.
Most curricula teach greedy as a list of problems where it happens to
work and ask you to memorize them. We're going to teach the
**exchange argument** — the actual proof technique — on one problem,
and then you'll know how to verify any future greedy claim yourself.

## The problem: activity selection

```
You have N activities, each with a start time s_i and finish time f_i.
You can attend at most one activity at a time. Return the MAXIMUM
number of activities you can attend.
```

Example:
```
[(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
```
Answer: 4 (attend `(1,4) → (5,7) → (8,11) → (12,16)`).

## The greedy claim

> **Sort activities by finish time. Scan in order; take an activity
> iff its start ≥ the finish of the last taken activity.**

```python
def select(activities: list[tuple[int, int]]) -> list[tuple[int, int]]:
    activities = sorted(activities, key=lambda a: a[1])
    chosen: list[tuple[int, int]] = []
    last_finish = float("-inf")
    for s, f in activities:
        if s >= last_finish:
            chosen.append((s, f))
            last_finish = f
    return chosen
```

That's the algorithm. Now: **why is it correct?**

## The exchange argument (the proof)

Claim: the greedy choice is *safe* — there exists an optimal
solution that includes it.

**Proof.** Let `g_1` be the activity greedy picks first (the one with
the earliest finish). Let `OPT` be any optimal solution. Sort `OPT`
by finish time; let its first activity be `o_1`.

Two cases:
1. **`o_1 == g_1`**: greedy and OPT agree on the first move. Continue
   the argument on the remaining activities (induction).
2. **`o_1 != g_1`**: by definition, `g_1` finishes no later than
   `o_1` (greedy picked the earliest-finishing activity). *Swap*
   `o_1` for `g_1` in OPT. The new schedule:
   - Has the same size as OPT (one in, one out).
   - Is still valid: `g_1` finishes ≤ when `o_1` did, so the next
     activity in OPT (whose start ≥ `o_1`'s finish) is still
     scheduleable. No conflict.
   So the swapped schedule is *also* optimal, and it includes `g_1`.

Either way, an optimal solution containing `g_1` exists. By
induction on the remaining activities, greedy is correct.

## What just happened

That argument has a name (**exchange argument**) and a shape:
1. Assume an optimal solution that *disagrees* with greedy at some
   step.
2. Show you can swap the disagreeing piece for greedy's choice
   *without losing optimality or validity*.
3. Conclude that an optimum exists that *agrees* with greedy.

When the swap doesn't preserve validity (Day 115's coin change is
the canonical failure: swapping a 5 for nothing leaves an unfillable
gap), the exchange argument fails, and so does greedy.

## When greedy works (the inventory)

The proof generalizes to other problems with similar swap-preserves
structure:

| Problem | Greedy choice | Why exchange works |
|---|---|---|
| Activity selection | earliest finish | swap doesn't break later starts |
| Huffman coding | merge two least-frequent | rebalancing swap preserves prefix-codes |
| Kruskal's MST | smallest edge that doesn't cycle | matroid structure (cycle property) |
| Dijkstra (non-negative weights) | nearest unvisited | shortest-path optimality |
| Fractional knapsack | best v/w ratio | divisibility means swap is local |

You don't need to memorize the table. You need: **before you trust
a greedy algorithm, write the exchange argument or admit it doesn't
go through.**

## Today's exercises

- **Fluency**: 5 small problems. For each, claim "greedy by X" and
  attempt the exchange argument. Two of the five fail; the
  diagnose helper points at *where* the swap breaks validity.
- **Guided**: implement activity selection by finish time.
- **Solo**: a different greedy problem — *minimum number of
  platforms* (railway scheduling). Sort by start, sweep, track
  overlap with a counter. The exchange argument is mechanical.
- **Apply**: read a real conference schedule (CSV); print the
  maximum non-overlapping talk subset.

## Now: open `fluency.py`
