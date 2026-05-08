---
day: day-021-what-is-hashing
phase: phase-1-python-core
module: module-04-dicts-sets-hashing
style: build-it
---
# Day 21 — Pretend dicts don't exist

You've been *using* O(1) dict lookups since Day 18. Today you build
your own (a tiny one) so the magic is no longer magic.

## The idea, in three steps

You have N "buckets" — a fixed-size list. To store a key, you:

1. Compute `hash(key)` — a deterministic int derived from the key's
   value.
2. Reduce that int to a bucket index: `i = hash(key) % N`.
3. Put `(key, value)` into bucket `i`.

To look up a key: same steps 1 and 2, then look in bucket `i`.

```python
# A toy hashmap built on a list-of-buckets.
class Tiny:
    def __init__(self, n_buckets=8):
        self.buckets = [[] for _ in range(n_buckets)]

    def _bucket_for(self, key):
        return self.buckets[hash(key) % len(self.buckets)]

    def __setitem__(self, key, value):
        bucket = self._bucket_for(key)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def __getitem__(self, key):
        for k, v in self._bucket_for(key):
            if k == key:
                return v
        raise KeyError(key)
```

## Why is this O(1) on average?

If `hash` spreads keys *uniformly* across buckets, each bucket holds
~`N_keys / N_buckets` items. CPython grows the bucket array so this
ratio stays small (around 1/3 to 2/3 — the **load factor**). So each
lookup walks a tiny list. That's the "O(1) average" you've been using.

The **worst** case is O(n): every key lands in the same bucket. In
practice good hash functions plus dynamic resizing keep that from
happening.

## Why must keys be hashable?

`hash(x)` must be:

1. **Stable** — the same x returns the same hash within a process.
2. **Consistent with equality** — if `a == b`, then `hash(a) == hash(b)`.

Mutable types (list, dict, set) can't satisfy this — if you put a list
in a dict, mutate the list, the bucket math breaks. Python prevents
this by making lists unhashable. Tuples *of hashables* are hashable;
that's why a tuple can be a dict key but a list cannot.

```python
hash((1, 2, "a"))   # works
hash([1, 2, 3])     # TypeError: unhashable type: 'list'
hash({1, 2})        # TypeError: unhashable type: 'set'
```

## Hash collisions are real and survivable

Two different keys can produce the same hash. The bucket holds a
*list*, so we walk it and compare with `==`. The hash narrows the
search; equality confirms the match. That's why a hashmap needs both
a hash function *and* an equality test.

## What lives in a CPython dict bucket

CPython is fancier than the toy above (open addressing, perturbation
probing, an "indices" array — see CPython's `Objects/dictobject.c` if
you're curious). But the model — *hash to a bucket, fall back to a
linear walk on collision* — is the same.

## Now: open `fluency.py`

You'll fix three small pieces of a `Tiny` hashmap. The tests will
pinpoint each one.
