---
day: day-032-list-dict-set-comprehensions
phase: phase-2-pythonic-tools
module: module-06-comprehensions-iterators-generators
style: pain
---
# Day 32 — The for-loop graveyard

You're cleaning up a teammate's code. You find this:

```python
upper_names = []
for name in names:
    if name:
        upper_names.append(name.upper())

by_id = {}
for user in users:
    by_id[user["id"]] = user

unique_tags = set()
for post in posts:
    for tag in post["tags"]:
        unique_tags.add(tag.lower())
```

Three loops. Three temporary containers. Three places where you have to
read four lines just to learn one fact: "uppercase the non-empty names."
The intent is buried under bookkeeping.

## The relief: comprehensions

Python lets you write the *result* directly, with the loop tucked inside:

```python
upper_names = [name.upper() for name in names if name]
by_id = {u["id"]: u for u in users}
unique_tags = {tag.lower() for post in posts for tag in post["tags"]}
```

Same output. Same speed (often faster, since the loop runs in C). One
line per intent. The shape of the brackets tells you the type:

- `[...]` → list
- `{key: value ...}` → dict
- `{...}` → set
- `(...)` → **not** a tuple — that's a generator (Day 33).

## The grammar

A comprehension is a single expression with three slots:

```
[OUTPUT for VARIABLE in ITERABLE if CONDITION]
```

You can stack `for` and `if` clauses. Read them top-to-bottom, left to
right, like nested loops:

```python
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
```

is exactly:

```python
pairs = []
for x in range(3):
    for y in range(3):
        if x != y:
            pairs.append((x, y))
```

## When *not* to use one

- If the body needs more than a single expression, write the loop.
- If the comprehension wraps to a third line, write the loop.
- If you're calling a side-effect function (`print`, `db.save`), write
  the loop. A comprehension that throws away its result is a code smell.

A comprehension is a *value*, not an action. If you want a value, reach
for it. If you want to do a thing N times, write the loop.

## Now: open `02_fluency.py`

Two for-loop graveyards to flatten into one-liners.
