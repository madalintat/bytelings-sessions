---
day: day-093-hash-table-chaining
phase: phase-4-data-structures
module: module-19-heaps-and-hash-tables
style: build-it
---
# Day 93 — A hash table, from scratch (chaining edition)

Pretend `dict` doesn't exist. You have a list, indexed by integer
positions. You want to look up "alice" -> 31 in O(1). The trick:
turn "alice" into an integer. That integer is the array index. The
function that does the turning is a **hash function**. The
data structure that wraps it all is a **hash table**.

```
"alice"  --hash--> 0xAB12...   --mod 8--> index 5  --> bucket[5]
```

`hash("alice")` is huge, so we mod it by the table size to land in
range. That's the index. Two different keys can land at the same
index — a **collision**. Collisions are not a bug; they're the whole
problem. Today's collision strategy is **chaining**: each slot in
the array holds a *list of key/value pairs*, and we walk that small
list to disambiguate.

```
slots:
   [0] -> []
   [1] -> [("bob", 22)]
   [2] -> []
   [3] -> [("alice", 31), ("eve", 28)]   <-- collision! both hash to 3
   [4] -> []
   ...
```

Within a bucket, we walk linearly. If buckets stay short, that walk
is essentially O(1) — and the overall table behaves like an O(1)
dictionary.

## The three operations

```python
def get(self, key):
    bucket = self.slots[hash(key) % len(self.slots)]
    for k, v in bucket:
        if k == key:
            return v
    raise KeyError(key)

def put(self, key, value):
    bucket = self.slots[hash(key) % len(self.slots)]
    for i, (k, _v) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)   # overwrite
            return
    bucket.append((key, value))
    self._size += 1
    if self._size / len(self.slots) > 0.75:
        self._resize()

def delete(self, key):
    bucket = self.slots[hash(key) % len(self.slots)]
    for i, (k, _v) in enumerate(bucket):
        if k == key:
            bucket.pop(i)
            self._size -= 1
            return
    raise KeyError(key)
```

Three patterns, all the same: hash the key, find the bucket, walk
the bucket. The only thing that's tricky is **resize**.

## Why resize?

If you let the table fill up, every bucket grows, walks slow down,
and your O(1) becomes O(n). The fix: when load factor (size /
slots) crosses some threshold (~0.75 is a common choice), allocate a
new larger array (typically double) and **re-hash every entry into
it**. The old indices are wrong because the modulus changed.

Resize is O(n), but it's amortized over the inserts: across n
inserts the total work is still O(n), so each insert is amortized
O(1). This is the same amortized argument that makes Python's `list`
append O(1).

## When to use one (vs. dict)

In production: use `dict`. CPython's dict is years of tuning. The
reason to write your own once is to *understand the algorithm*: when
your code "feels slow" and you suspect a hash issue, you'll know
what to look at. (Spoiler: it's almost always a bad `__hash__`
implementation that puts everything in one bucket.)

## When chaining is the right choice

Chaining is robust under high load and simple to reason about. The
alternative — **open addressing**, tomorrow's day — is more
cache-friendly but has subtler edge cases. Most modern hash tables
(including CPython's `dict`!) use open addressing. We learn chaining
first because the *concept* is clearer; then we'll see why open
addressing won.

## Now: open `02_fluency.py`

Two helpers, each with one wrong line.
