---
day: day-020-defaultdict-and-counter
phase: phase-1-python-core
module: module-04-dicts-sets-hashing
style: pain
---
# Day 20 — The `if key not in d` ceremony

Day 18 you wrote this:

```python
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
```

Now imagine you're grouping items by their first letter:

```python
groups = {}
for w in words:
    key = w[0]
    if key not in groups:
        groups[key] = []
    groups[key].append(w)
```

Look at that "if key not in d, initialize" dance. Three lines for one
idea. Multiply by every grouping/counting you'll ever do. That's a lot
of ceremony.

## The fix #1: `defaultdict`

```python
from collections import defaultdict

groups = defaultdict(list)
for w in words:
    groups[w[0]].append(w)
```

`defaultdict(factory)` is a dict subclass. When you read a missing
key, it calls `factory()` and stores the result automatically. So
`groups["a"]` on an empty `groups` returns a fresh `[]`, stored under
"a", ready to `.append`. Three lines collapse to one.

| Factory | Use for |
|---|---|
| `list` | grouping items by key |
| `int` | counting (returns 0) |
| `set` | unique items per key |
| `dict` | nested dicts (`d[k1][k2]`) |
| `lambda: "default"` | any custom default |

## The fix #2: `Counter`

For pure counting, there's an even tighter tool:

```python
from collections import Counter

counts = Counter(text.split())
counts.most_common(3)        # [('the', 12), ('cat', 9), ...]
```

A `Counter` is a dict subclass where missing keys read as 0 (no
KeyError). It also adds:

- `most_common(n)` — top n by count.
- `+`, `-` — combine counters: `c1 + c2` adds counts.
- `total()` — sum of all counts (Python 3.10+).
- Construct from any iterable, dict, or kwargs.

## A side-by-side, one more time

Plain dict:

```python
counts = {}
for x in items:
    counts[x] = counts.get(x, 0) + 1
```

defaultdict(int):

```python
counts = defaultdict(int)
for x in items:
    counts[x] += 1
```

Counter:

```python
counts = Counter(items)
```

All three produce the same answer. Pick by intent: `Counter` says "I'm
counting." `defaultdict(list)` says "I'm grouping." Plain dict, with
`get`, says "I want to be explicit and stay close to the standard
type."

## A small gotcha

Reading from a `defaultdict` *creates* the missing key. That's
sometimes surprising:

```python
d = defaultdict(list)
"missing" in d         # False
d["missing"]           # [] — and now d["missing"] exists
"missing" in d         # True
```

Use `.get(k)` if you want a non-creating read, or convert to a plain
dict (`dict(d)`) before handing it to code that doesn't expect this.

## Now: open `fluency.py`

Three functions that do the "if not in d" dance. Replace with
`defaultdict` or `Counter`.
