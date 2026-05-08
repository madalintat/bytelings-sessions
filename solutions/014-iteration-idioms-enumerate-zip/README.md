---
day: day-014-iteration-idioms-enumerate-zip
phase: phase-1-python-core
module: module-03-lists-and-bigo
style: pain
---
# Day 14 — The C-style `for i in range(len(...))` smell

You start writing a function. You need both the index and the item.
You write what your last language taught you:

```python
items = ["alpha", "bravo", "charlie"]
for i in range(len(items)):
    print(f"{i}: {items[i]}")
```

It works. But every Python reviewer's eyebrow goes up. Why?

- `range(len(items))` is verbose.
- `items[i]` is an extra index lookup the loop already had access to.
- You broke the link between "I'm walking items" and "I'm using i".

## The fix: `enumerate`

```python
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

`enumerate(iterable, start=0)` yields `(index, item)` pairs. It costs
one tuple per step (negligible) and the code reads exactly like the
intent. **Use it any time you find yourself writing `range(len(...))`**.

## A second smell: parallel index loops

You have two lists, same length, you want to use them together. The
old way:

```python
names  = ["alice", "bob", "carol"]
scores = [90, 85, 92]
for i in range(len(names)):
    print(f"{names[i]}: {scores[i]}")
```

## The fix: `zip`

```python
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

`zip` walks two (or more) iterables in lockstep, yielding tuples. It
**stops at the shortest** input — important. If you need it to error
on length mismatch, use `zip(a, b, strict=True)` (Python 3.10+).

## Combining them

Want index + two parallel lists? Just compose:

```python
for i, (name, score) in enumerate(zip(names, scores)):
    ...
```

Read it right-to-left: zip pairs them, enumerate numbers the pairs.

## A short table of "what loop do I want?"

| You want | Use |
|---|---|
| Just the items | `for x in items:` |
| Items + their position | `for i, x in enumerate(items):` |
| Items from two lists in parallel | `for a, b in zip(xs, ys):` |
| Pairs (curr, next) | `for a, b in zip(xs, xs[1:]):` |
| Items + position + parallel | `for i, (a, b) in enumerate(zip(xs, ys)):` |
| The list, just numbered for output | `list(enumerate(xs))` |

## Two more idioms worth seeing once

```python
for i, line in enumerate(open("file"), start=1):  # 1-based line numbers
    ...

# Building a dict from two parallel lists:
phonebook = dict(zip(names, scores))   # {'alice': 90, 'bob': 85, ...}
```

## Now: open `02_fluency.py`

Three loops are using the C-style smell. Convert each to the pythonic
idiom.
