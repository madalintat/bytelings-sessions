---
day: day-018-dict-basics
phase: phase-1-python-core
module: module-04-dicts-sets-hashing
style: story
---
# Day 18 — The phonebook your boss won't stop adding to

Tuesday, 11 AM. Your boss slacks you a list of contacts. Then another.
Then another. Each time he wants you to "find Maria's number" or
"replace Bob's number with this new one" or "is Alice in the list?"

You started with a list of `(name, phone)` tuples. Every lookup is a
linear scan. With 50 contacts that's fine. He's at 15,000 now and your
script feels sluggish.

You switch to a `dict`:

```python
contacts = {
    "Alice": "415-555-0101",
    "Bob":   "415-555-0102",
    "Maria": "415-555-0103",
}

contacts["Maria"]               # '415-555-0103'  — O(1) lookup
contacts["Bob"] = "555-9999"    # update — O(1)
contacts["Bytelinger"] = "415-555-0144"   # add — O(1)
"Alice" in contacts             # True — O(1)
del contacts["Bob"]             # remove — O(1)
len(contacts)                   # how many keys
```

Your script gets instant.

## What a dict actually is

A dict is a **key → value** map. Each key is unique. Internally,
Python keeps a hash table (Day 21). The headline guarantees:

- **Lookup, insert, delete by key: O(1) on average.** That's the
  superpower vs. lists.
- **Keys must be hashable** (immutable types: int, str, tuple of
  hashables). Lists can't be keys; tuples can.
- **Insertion order is preserved** (Python 3.7+). Iteration walks the
  keys in the order they were first inserted.

## The four ways to read

```python
contacts["Alice"]              # KeyError if missing
contacts.get("Alice")          # None if missing
contacts.get("Alice", "?")     # default if missing — your daily bread
"Alice" in contacts            # bool, no read
```

Pick `.get(...)` when "missing" is normal. Pick `[...]` when missing
is a real bug — letting it raise tells you something's broken.

## Iterating: three views

```python
for key in contacts:                  # keys
    ...
for key in contacts.keys():           # same as above
    ...
for value in contacts.values():
    ...
for key, value in contacts.items():    # most useful
    ...
```

Use `.items()` whenever you need both. It's the dict version of
`enumerate` — pythonic and fast.

## A real-world idiom: count things

```python
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
```

That `.get(word, 0) + 1` pattern is one of the top-5 things you'll
write across your career. Day 20 shows the cleaner `Counter` for the
exact same job.

## The `dict()` constructor variants

```python
dict()                            # {}
dict(a=1, b=2)                    # {'a': 1, 'b': 2}
dict([('a', 1), ('b', 2)])        # from pairs
dict(zip(keys, values))           # from parallel lists
{k: f(k) for k in keys}           # dict comprehension (Phase 2)
```

## Now: open `fluency.py`

Three small dict ops are wrong. Patch them.
