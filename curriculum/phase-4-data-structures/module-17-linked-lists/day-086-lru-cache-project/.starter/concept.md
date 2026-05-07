---
day: day-086-lru-cache-project
phase: phase-4-data-structures
module: module-17-linked-lists
style: story
---
# Day 86 — Build an LRU cache that survives traffic

A web service is paying for an upstream API: ten cents per call, no
free tier. You're the on-call. The boss says: *cache it.* But memory
isn't free either, and most cached entries are never re-asked. So
you cap the cache at, say, 1000 entries, and when a 1001st key
arrives you have to throw something out.

Which one?

The standard answer for the last 50 years: throw out the **least
recently used** key. The one nobody's touched in the longest. The
intuition: if it's been a while, it'll probably be a while longer. The
data structure that makes this fast is what you'll build today.

## The problem with naive solutions

A `dict` makes lookups O(1). Great. But `dict` doesn't track *order
of use*. A first attempt might walk every entry to find the oldest —
**O(n) eviction**. On a hot path, that's the whole problem all over
again.

You need:
- **O(1) lookup by key**
- **O(1) update of "most recently used"**
- **O(1) eviction of the least recently used**

A single data structure can't do all three. So you combine two:

```
dict (key -> Node)        DoublyLinkedList (head=newest, tail=oldest)
{
  "alice" -> [Node A]      head -> [B] <-> [A] <-> [C] <-> [D] <- tail
  "bob"   -> [Node B]              MRU                     LRU
  ...
}
```

The dict gives you O(1) "find the node for this key." The doubly
linked list gives you O(1) splice (move to head) and O(1) tail
removal. Together, all three operations are O(1).

This combination — **hash map + doubly linked list** — is one of
the most useful patterns in the whole curriculum. It comes up in
caches, in MRU lists, in editor history, in OS page tables. Once you
see it, you see it everywhere.

## The two operations

```python
def get(self, key):
    if key not in self.map:
        return None                    # cache miss
    node = self.map[key]
    self._move_to_front(node)          # O(1) splice
    return node.value[1]               # node holds (key, value)

def put(self, key, value):
    if key in self.map:                # update existing
        node = self.map[key]
        node.value = (key, value)
        self._move_to_front(node)
        return
    if len(self.map) == self.capacity: # evict LRU
        oldest = self.list.tail
        del self.map[oldest.value[0]]
        self.list.delete(oldest)
    new_node = self.list.prepend((key, value))
    self.map[key] = new_node
```

Notice we store the **key inside the node**. Why? Because when we
evict the tail, we need to remove that key from the dict — and we get
to the tail via the list, not the dict. Without the key inside, you'd
have no way to know which dict entry to remove.

## The thing the standard library already has

`functools.lru_cache` is decorator-shaped LRU. It does exactly this
under the hood. But the goal today isn't to use a black box — it's to
*build* the box, so when it shows up in a system design question or a
hot path you're profiling, you know what's inside.

## Now: open `02_fluency.py`

Two tiny LRU helpers, each near-correct.
