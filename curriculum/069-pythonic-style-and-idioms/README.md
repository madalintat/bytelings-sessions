---
day: day-069-pythonic-style-and-idioms
phase: phase-3-quality-production
module: module-13-reading-refactoring-style
style: compare
---
# Day 69 — Two ways, one Pythonic

There's a phrase old-school Pythonistas use: "code that *reads* like
Python." It's a real thing. Pythonic code is shorter, the intent
sits at the top of the line instead of buried under bookkeeping, and
*you can read it as if it were English*. Today, side-by-side.

## Five idiom comparisons

### 1. Iteration

```python
# Java-flavored Python:
for i in range(len(items)):
    print(i, items[i])

# Pythonic:
for i, item in enumerate(items):
    print(i, item)
```

`enumerate` is the answer to "I want the index AND the item." If you
ever write `range(len(...))`, stop and ask whether `enumerate` or
`zip` would do.

### 2. Building lists

```python
# C-flavored:
squares = []
for x in xs:
    squares.append(x * x)

# Pythonic:
squares = [x * x for x in xs]
```

Comprehensions are not just shorter — they signal *intent*. The line
"build a list by transforming each x" is one Python expression. The
imperative version is three lines that you have to mentally
reconstruct into the same idea. (Don't go too far: nested or
filter-heavy comprehensions can become unreadable. If the line wraps,
go back to a `for`-loop.)

### 3. Default values for missing keys

```python
# LBYL with redundant check:
if key not in counts:
    counts[key] = 0
counts[key] += 1

# Pythonic:
counts[key] = counts.get(key, 0) + 1

# Even more Pythonic for this exact case:
from collections import defaultdict
counts = defaultdict(int)
counts[key] += 1
```

### 4. Truthiness vs explicit comparisons

```python
# Verbose and slightly wrong:
if len(items) > 0:
    ...
if name == "":
    ...

# Pythonic:
if items:           # empty list is falsy
    ...
if not name:        # empty string is falsy
    ...
```

Caveat: when you specifically mean "is None," write `if x is None:`,
not `if not x:` — `0`, `[]`, and `""` are all falsy but not `None`.

### 5. Unpacking instead of indexing

```python
# Indexing:
first = pair[0]
second = pair[1]

# Pythonic:
first, second = pair
```

Goes further with `*rest`:

```python
head, *body, tail = [1, 2, 3, 4, 5]
# head=1, body=[2,3,4], tail=5
```

## "Pythonic" is not a religion

The point isn't conformity. The point is that idiomatic Python tends
to be **shorter, more correct, and more searchable**. Searchable
matters: when a future reader (you, in six months) sees `for i, x in
enumerate(items):` they recognize it instantly. They don't have to
parse it. That's compounding readability.

The Zen of Python's "readability counts" lives here. Compare the two
versions of each idiom above, and ask which one you'd rather read in
a 4 AM page-out.

## Now: open `fluency.py`

Three small functions written in non-Pythonic style. Rewrite them.
