---
day: day-084-singly-linked-list
phase: phase-4-data-structures
module: module-17-linked-lists
style: build-it
---
# Day 84 — A linked list, from scratch

Pretend Python's `list` doesn't exist and you have one tool: an
object with two slots, a value and a "next" pointer. With those
two slots and nothing else, you can make a sequence of values that
grows from either end without copying anything.

That's a **singly linked list**. Each node holds a value and a
reference to the next node. The whole list is identified by a single
reference: its **head**. The end is whichever node's `next` is None.

```
head -> [1|*] -> [2|*] -> [3|*] -> None
```

## Why it exists when Python already has `list`

For most everyday code, you should use `list`. It's faster, denser in
memory, and supports random access. But linked lists win in three
specific situations:

1. **Insertion / deletion in the middle is O(1)** — once you have a
   pointer to the node, you just rewire two `next` pointers. With
   `list`, the same operation is O(n) because everything shifts.
2. **Memory grows one node at a time** — there's no over-allocation,
   no reallocation copy. Useful when each item is large.
3. **They're a building block for other structures** — queues,
   adjacency lists, hash-table chains, the OS process table. Every
   tree is essentially a linked structure.

The cost: you can't index in O(1). To get item *k*, you walk *k*
nodes from the head. Every traversal is O(n). And each node carries
the overhead of a pointer.

When you reach for it: when you'll do many splice / insert / delete
operations and rarely need indexed access. Otherwise: `list`.

## The two pieces

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head: Node | None = None
        self._size: int = 0
```

A node is two slots. The list is one slot (the head) plus a size
counter so `len(ll)` is O(1) instead of a walk.

## The operations you'll write today

- `prepend(x)` — new node becomes the head. **O(1).**
- `append(x)` — walk to the end, attach. **O(n).**
- `pop_front()` — remove and return head. **O(1).**
- `__len__`, `__iter__`, `__contains__` — basic dunder support.

Notice prepend is cheap, append is expensive — the *opposite* of a
Python `list`. Linked lists are best when you're working at the head.
We'll fix the slow append by adding a `tail` pointer in tomorrow's
doubly-linked variant.

## Now: open `02_fluency.py`

A node-walking helper has two off-by-one bugs.
