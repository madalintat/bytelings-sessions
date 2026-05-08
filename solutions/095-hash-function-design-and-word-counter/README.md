---
day: day-095-hash-function-design-and-word-counter
phase: phase-4-data-structures
module: module-19-heaps-and-hash-tables
style: detective
---
# Day 95 — The case of the slow word counter

You inherited a script that counts word frequencies in a 5GB text
corpus. It used to run in 90 seconds. Today it ran for 25 minutes
before you killed it. Nothing changed in the code. The corpus didn't
quadruple in size — it grew 5%. So why is it 16x slower?

You profile it. The hot loop is in your custom `HashMap.put`. You
add a print statement to your `__hash__`:

```python
class WordKey:
    def __init__(self, word):
        self.word = word
    def __hash__(self):
        return len(self.word)        # <-- the smoking gun
    def __eq__(self, other):
        return self.word == other.word
```

You used `len(word)` as the hash. *It returns the same number for every
word of the same length.* So all 4-letter words hash to bucket 4. All
5-letter words hash to bucket 5. Your "hash table" is actually 8
linked lists. Every lookup walks the list. The lookup is **O(n) per
call**, multiplied by n calls — **O(n²)**. That's where the 16x went.

## The two crimes

1. **Hash collision is correctness-safe but performance-deadly.**
   Two different words with the same hash still get the right answer
   thanks to your bucket walk — but they walk together, dragging
   every lookup down to linear time.
2. **A "smart" hash that ignores most of the input is a bad hash.**
   `__hash__` should look at *every byte that affects equality*,
   otherwise two un-equal-but-same-hash values are guaranteed
   collisions in disguise.

## What makes a good hash function?

Three properties, in order of importance:

1. **Equal values must hash equal.** `a == b` must imply
   `hash(a) == hash(b)`. (The reverse isn't required.)
2. **Different values should hash differently** (probabilistically).
   Ideally, every output value is equally likely.
3. **Cheap to compute.** Hashing happens on every lookup; if it's
   slow, the table is slow.

The classical-but-good string hash (used by old Java) is
**polynomial rolling hash**:

```python
def djb2(s: str) -> int:
    h = 5381
    for ch in s:
        h = (h * 33 + ord(ch)) & 0xFFFFFFFF
    return h
```

Each character matters, multiplied by a prime-ish power so the
contribution of each position is different. Reordering the same
letters gives a different hash. Adding a letter changes the hash a
lot. The mask keeps the result a 32-bit integer.

A second classic: **FNV-1a**:

```python
def fnv1a(s: str) -> int:
    h = 0x811c9dc5
    for ch in s:
        h = ((h ^ ord(ch)) * 0x01000193) & 0xFFFFFFFF
    return h
```

These are not cryptographic, just well-distributed and fast. For a
hash table, that's all you want.

## The fix in your real code

```python
class WordKey:
    __slots__ = ("word", "_hash")
    def __init__(self, word):
        self.word = word
        self._hash = djb2(word)        # cache it
    def __hash__(self):
        return self._hash
    def __eq__(self, other):
        return isinstance(other, WordKey) and self.word == other.word
```

Now words distribute evenly across all buckets. The 25-minute job
finishes in under two minutes. The bug wasn't a bug — every line
"worked." It was an O() bug, the kind where the *symptom* shows up
months after the cause is shipped. Profiling and `__hash__` design
are how you find these.

## What you'll build today

A small word-frequency tool that uses a hash function you wrote.
You'll see the perf cliff yourself: a deliberately bad hash vs a
good one, on the same input.

## Now: open `fluency.py`

A polynomial rolling hash with one bug.
