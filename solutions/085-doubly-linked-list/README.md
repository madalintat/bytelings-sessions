---
day: day-085-doubly-linked-list
phase: phase-4-data-structures
module: module-17-linked-lists
style: tour
---
# Day 85 — A tour of the doubly linked list

Yesterday's singly linked list had two weaknesses: appending at the
end was O(n), and you couldn't walk backwards. Both fix with one
small change to the node:

```python
class Node:
    __slots__ = ("value", "prev", "next")
```

A `prev` pointer in addition to `next`. Now every node knows the one
before it as well as the one after. The list keeps two pointers
instead of one: a `head` and a `tail`. With those, both ends are
cheap.

```
None <- [a] <-> [b] <-> [c] -> None
        head            tail
```

## What gets fast

- **append** — jump to `tail`, attach. **O(1)** instead of O(n).
- **pop_back** — same. **O(1)**.
- **delete a node you already have a reference to** — rewire its
  `prev.next` and `next.prev`, no walk. **O(1)**.

That last one is the killer feature. If your code holds direct
references to nodes (because, say, you're building an LRU cache —
spoiler: you are, tomorrow), you can splice nodes in and out of the
middle of the list in constant time. With a singly linked list, you'd
have to find the previous node by walking from the head: O(n).

## What stays slow

Index access is still O(n). The list is a chain, not an array. For
random access, use `list`. The doubly linked list is a *splice
machine* — that's its only superpower.

This is also the structure underlying `collections.deque`. (Roughly —
deque uses a chain of fixed-size *blocks* rather than per-element
nodes, for memory efficiency. But conceptually it's a doubly linked
list of blocks.)

## The tricky operation: `delete(node)`

```python
def delete(self, node: Node) -> None:
    if node.prev is not None:
        node.prev.next = node.next
    else:
        self.head = node.next      # node was the head
    if node.next is not None:
        node.next.prev = node.prev
    else:
        self.tail = node.prev      # node was the tail
    self._size -= 1
```

Four pointer rewrites and two boundary cases. If `prev` is None, we
were at the head; the new head is `next`. If `next` is None, we were
at the tail; the new tail is `prev`. Both can be true (single-element
list goes empty). Always update the size.

The pattern of "always check prev/next for None at the boundaries" is
half of why doubly linked list code looks long. The other half is the
careful order: rewire neighbors *before* losing your last reference
to the node, or you'll lose the chain.

## When to reach for one

- **You need O(1) inserts/deletes anywhere given a node reference.**
- You're building an LRU cache, an MRU queue, or a freelist.
- You're maintaining a "live" ordered set where users hold tokens
  (the node reference) to remove their items quickly.

For 99% of "I want a list" cases: still use Python's `list` or
`deque`. The doubly linked list earns its keep when you need to splice
arbitrary nodes in O(1).

## Now: open `fluency.py`

A `delete` helper has the boundary cases backwards.
