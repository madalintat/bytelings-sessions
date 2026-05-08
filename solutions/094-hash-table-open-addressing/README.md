---
day: day-094-hash-table-open-addressing
phase: phase-4-data-structures
module: module-19-heaps-and-hash-tables
style: compare
---
# Day 94 — Two ways to handle a collision

You wrote a hash map yesterday. Two different keys hashed to the same
slot. You handled it by stuffing both into a list at that slot. That's
**chaining**. There's a second strategy. Let's compare them
side-by-side.

## Strategy A: chaining (yesterday)

```
slot 3:  [("alice", 31), ("eve", 28)]    <- both keys hashed to 3
```

Each slot holds a list of entries. On collision, append. On lookup,
walk the list.

## Strategy B: open addressing (today)

```
slot 3:  ("alice", 31)
slot 4:  ("eve",   28)        <- "eve" wanted slot 3 but it was taken,
                                 so we walked one step right
slot 5:  ("bob",   22)
```

Every entry sits **directly in the slot array**. No nested list. On
collision, you **probe** to the next slot, then the next, until you
find an empty one. On lookup, you start at the hashed slot and walk
forward until you find your key, or hit a true empty.

The simplest probing rule is "go one step at a time," called **linear
probing**. There are fancier rules (quadratic probing, double
hashing) but linear is the easiest to reason about.

## The comparison

| Aspect | Chaining | Open addressing |
|---|---|---|
| Storage | array of lists | flat array |
| Memory per entry | extra list overhead per slot | denser; no per-slot list |
| Cache behavior | each bucket is a separate alloc | linear probes hit cached slots |
| Max load factor | works fine at 0.9+ | needs to stay <~0.7 |
| Delete | trivial: remove from bucket | tricky: "tombstones" |
| Implementation | simpler | subtler |

The CPython `dict` and most modern fast hash tables use **open
addressing**, even though chaining is conceptually simpler. The
reason: cache locality. Walking 4 contiguous array slots is faster
than chasing 4 linked-list pointers.

## The delete problem

Here's the subtlety. With chaining, deleting "eve" just removes one
list entry. The bucket at slot 3 still has "alice" so future lookups
for "alice" still work.

With open addressing, deleting "eve" would empty slot 4. But "eve"
is at slot 4 because slot 3 was full when she was inserted —
implying *something else* hashed to 3 and bumped her over. If we
*also* try to look up "bob" at slot 5, we may have walked through
slot 4 to find him; emptying it would break the chain. We'd stop at
the empty slot 4, conclude "bob" isn't there, and we'd be wrong.

The fix: a **tombstone**. When you delete, mark the slot as
"deleted" rather than truly empty. Lookups skip past tombstones.
Inserts may reuse them. The dance is intricate enough that getting
delete right is the rite of passage for open addressing.

## When each one wins

- **Chaining**: when entries are big or load factor will go very
  high. Keys with bad hash functions degrade gracefully.
- **Open addressing**: when you want raw speed and can keep load
  bounded. Used by Python, Java, Go.

## What you'll build today

A `HashMapOA` with open addressing + linear probing. Same external
API as yesterday's `HashMap`, but now with tombstones for delete.
After this you'll have built both strategies and can read any hash
table source with confidence.

## Now: open `fluency.py`

Two probing helpers, each missing one line.
