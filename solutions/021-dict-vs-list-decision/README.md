---
day: 021-dict-vs-list-decision
phase: phase-1-python-core
module: module-04-hashing-dicts-sets-and-bigo
style: compare
---
# Day 21 — Same task, two shapes

You have a roster of users. Each has a unique `id`, a `name`, and an
`active` flag. Two ways to model it. Both work. Which do you pick?

### Snippet A — list of dicts
```python
users = [
    {"id": 17, "name": "Alice", "active": True},
    {"id": 32, "name": "Bob",   "active": False},
    {"id": 41, "name": "Carol", "active": True},
]

def by_id(users, target):
    for u in users:
        if u["id"] == target:
            return u
    return None
```

### Snippet B — dict of dicts (id → user)
```python
users = {
    17: {"name": "Alice", "active": True},
    32: {"name": "Bob",   "active": False},
    41: {"name": "Carol", "active": True},
}

def by_id(users, target):
    return users.get(target)
```

For "give me user 32," A is **O(n)**. B is **O(1)**. With 50 users
the difference is invisible. With 50,000 users called from a web
endpoint, B is the only sane choice.

## When to pick what

| Question | Pick |
|---|---|
| "Give me item N in order" | list (`users[i]`) |
| "Give me the item with this unique id" | dict (`users[id]`) |
| "Are there duplicates? In what order?" | list |
| "Iterate by insertion order" | list (or dict — Py 3.7+) |
| "Sort by some field" | list (then `sorted(..., key=...)`) |
| "Membership test in a hot loop" | set or dict |
| "All three (order + lookup + dedup)" | dict where keys are the ids |

## A common pitfall: the "list of dicts of stuff" trap

```python
# Don't search by linear scan when ids are unique:
for u in users:
    if u["id"] == target_id:
        return u
```

If you find yourself writing that loop and `id` is unique, the answer
is almost always to **switch to a dict keyed by id**, OR to build an
index once if you can't change the storage:

```python
index = {u["id"]: u for u in users}     # one pass, O(n)
index[target_id]                         # O(1) per lookup after that
```

That dict comprehension is one of the most useful 25-character spells
in Python.

## When the list shape really is right

- The order itself is data (stack, queue, log, sequence of events).
- There's no natural unique key (rows of a CSV with no id column).
- You'll iterate way more than you'll lookup-by-key.
- Items are not hashable (rare in business code, common in scientific
  code with arrays).

## A small worked decision

You're loading 100,000 contacts and need:

- "Show all of them sorted by name" → list, sort by name.
- "Show the one with phone X" → dict keyed by phone.

That's two indices. Both are fine to build. The trick: build them
once, share-the-data: each contact dict is one Python object held in
both indices (Day 4 — same object, two names).

## Now: open `fluency.py`

Three small choose-your-shape exercises. Pick the right structure and
implement.
