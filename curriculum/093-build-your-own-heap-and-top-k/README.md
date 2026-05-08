---
day: 093-build-your-own-heap-and-top-k
phase: phase-4-data-structures
module: module-19-heaps-and-hash-tables
style: build-it
---
# Day 93 — A heap, from scratch

Pretend `heapq` doesn't exist. You're going to write the two
operations that make a heap a heap: **sift-up** (after inserting at
the end) and **sift-down** (after replacing the root with the last
item). Once those two work, push, pop, and heapify all fall out of
them.

## The plan in one paragraph

A min-heap is stored in a flat list. Index 0 is the smallest. Parent
of index `i` is `(i-1)//2`; children are `2i+1` and `2i+2`.

- **push** = append to the end, then sift up (swap with parent while
  smaller).
- **pop** = grab index 0 (the answer), move the last item to index
  0, shrink the list, then sift down (swap with smaller child while
  larger).
- **heapify** = sift down from the middle of the array outward, in
  reverse index order. O(n) (counterintuitively cheaper than n
  pushes).

Two helpers, three public methods. That's the whole structure.

## Sift up

```python
def _sift_up(self, i):
    while i > 0:
        parent = (i - 1) // 2
        if self.data[i] < self.data[parent]:
            self.data[i], self.data[parent] = self.data[parent], self.data[i]
            i = parent
        else:
            return
```

You're at index `i`. Compare with your parent. If you're smaller,
swap and walk up. Stop when you're no longer smaller, or when you're
at the root. **O(log n)** because each step halves your index.

## Sift down

```python
def _sift_down(self, i):
    n = len(self.data)
    while True:
        left, right = 2*i + 1, 2*i + 2
        smallest = i
        if left  < n and self.data[left]  < self.data[smallest]:
            smallest = left
        if right < n and self.data[right] < self.data[smallest]:
            smallest = right
        if smallest == i:
            return
        self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
        i = smallest
```

The mirror of sift-up. Look at *both* children, pick the smaller
one, swap if it's less than you. The "compare against the smaller
child" detail is the most common bug. If you forget and just compare
to the left child, your invariant breaks the moment the right child
is the smaller one.

## Where this gets used

The textbook reason to know all this: **top-k queries.** You have a
billion log lines and want the 1000 longest. You can't sort them
all. You can't even hold them all in memory in one batch.

The trick: keep a **min-heap of size k**. Walk every item in the
stream. If the heap has fewer than k items, push. Otherwise, if the
new item is bigger than the heap's minimum, replace the minimum
(`heappushpop`). After the stream ends, the heap holds the top k.

Time: O(n log k). Space: O(k). That's the whole game.

```python
def top_k(stream, k):
    h: list[int] = []
    for x in stream:
        if len(h) < k:
            heapq.heappush(h, x)
        elif x > h[0]:
            heapq.heapreplace(h, x)
    return sorted(h, reverse=True)
```

## When to roll your own (vs use `heapq`)

In production: use `heapq`. It's C-fast and well-tested. The reason
to write your own once is to *understand the invariant*, so when a
performance bug shows up — "why is my priority queue slow?" — you
can think about the data structure, not the API. After today, you'll
read the `heapq` source like a normal Python file.

## Now: open `fluency.py`

Two heap helpers, each missing one critical detail.
