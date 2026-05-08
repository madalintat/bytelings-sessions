---
day: day-073-why-is-this-slow
phase: phase-3-quality-production
module: module-14-logging-profiling-perf
style: detective
---
# Day 73 — The case of the program that got slower the more you fed it

A user reports: "Your dedupe tool worked fine on my 10K record CSV.
On the 100K one it's been running for an hour." You profile. The
hotspot is a function called `is_seen`. You read it:

```python
seen = []
for record in records:
    if record.id not in seen:
        seen.append(record.id)
        process(record)
```

There it is. The bug isn't a bug. The code is *correct*. It's just
**asymptotically wrong** — the data structure is bullying the algorithm.

## The clue: `not in` on a list is O(n)

`x not in some_list` walks the list. With 100K records, every check
scans up to 100K items. That's ~10 billion comparisons total. The fix:

```python
seen = set()
for record in records:
    if record.id not in seen:
        seen.add(record.id)
        process(record)
```

`x not in some_set` is O(1) average (hash lookup). 100K checks now
cost 100K operations. From "an hour" to "less than a second."

## The detective's checklist

When a function is slow, run through these in order. The bug is
almost always one of them:

| Suspect | How to spot it | Fix |
|---|---|---|
| **Wrong data structure** | `in`/`remove`/`index` on a list inside a loop | Use a set/dict |
| **Quadratic loop** | Nested loops, both over the same input | Sort + scan, or a set, or a dict-as-index |
| **Repeated work** | Same `len()`/`getattr`/regex compile inside the loop | Hoist outside |
| **Reading the world too often** | `Path.read_text()` called per row | Read once, parse once |
| **String building with `+=`** | Loop concatenates a string | `"".join(parts)` |
| **Chatty I/O** | One DB call per record | Batch / fetch_all |

## The mental model: "what shape is this loop?"

For every loop, ask:

- What's `n`? (loop iterations)
- What does each iteration cost? (1, log n, n, n²?)
- Total? (multiply)

If iteration cost includes a list lookup over `n` items, you wrote an
n² algorithm. The CPU doesn't care that you didn't mean to.

## Quick wins from string-building to caching

### `+=` on strings is quadratic

```python
out = ""
for s in parts:
    out += s        # O(n²) total
# Replace with:
out = "".join(parts)
```

CPython sometimes optimizes the first form away, but only sometimes.
`"".join` always wins, always reads correctly, always.

### `lru_cache` for pure functions

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
```

If the function is pure (same input -> same output, no side effects)
and is called with the same args repeatedly, `lru_cache` is a free
speedup. Don't sprinkle it on impure functions — you'll cache stale
results.

### `set` operations beat manual loops

```python
common = [x for x in a if x in b]   # O(n*m)
common = list(set(a) & set(b))      # O(n + m)
```

## The temptation to micro-optimize

Don't replace `for x in xs:` with `for i in range(len(xs)):` "for
speed." Don't inline functions to skip a call. Modern CPython is
fast. The big wins (1000x or more) come from algorithmic changes:
list -> set, n² -> n. Micro-optimizations buy you a percent. Find
the algorithmic win, ship it, move on.

## Now: open `fluency.py`

A function that's accidentally O(n²). One-line fix.
