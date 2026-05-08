---
day: day-089-bst-insert-search
phase: phase-4-data-structures
module: module-18-trees-and-bst
style: build-it
---
# Day 89 — A binary search tree, from scratch

Pretend `dict` and `set` don't exist. You want to keep a collection
of comparable values and answer two questions fast: *is X in here?*
and *here's a new X, please remember it.* Linear search through a
list is O(n). A sorted list lets you binary-search in O(log n) but
inserts shift everything — O(n).

You can do better. A **binary search tree** does both lookup and
insert in O(log n) on average, by giving the tree itself the
search-friendly shape:

> For every node N, **all values in N's left subtree are < N.value**,
> and **all values in N's right subtree are > N.value**.

That's it. That's the whole rule. Apply it everywhere, recursively.

```
            50
           /  \
         30    70
        /  \   / \
       20  40 60 80
```

To search for 60: start at 50. 60 > 50, go right. Land on 70. 60 < 70,
go left. Land on 60. Found, in 3 hops out of 7 nodes. With more nodes
the saving compounds — a balanced BST with a million keys is searched
in about 20 hops.

## Insert

Insert is search-with-a-twist: you walk the tree the same way you'd
search, and when you fall off the end (hit a None child), you put
your new node there. The key invariant is preserved automatically
because you only ever go in the direction the new value belongs.

```python
def insert(root, x):
    if root is None:
        return TreeNode(x)
    if x < root.value:
        root.left = insert(root.left, x)
    elif x > root.value:
        root.right = insert(root.right, x)
    # if x == root.value: ignore (set semantics)
    return root
```

This is the canonical BST insert pattern. Notice the function
*returns* the (possibly new) root of the subtree it touched, and the
caller assigns it back: `root.left = insert(root.left, x)`. This is
the cleanest way to handle the case where the subtree was empty —
no separate special case for "tree is empty entirely."

## Search

The same walk, returning True/False (or the node, depending on what
you need):

```python
def contains(root, x):
    if root is None:
        return False
    if x == root.value:
        return True
    if x < root.value:
        return contains(root.left, x)
    return contains(root.right, x)
```

## When is the BST O(log n)?

When it's balanced. **A BST built from sorted insertions is a linked
list** — it skews entirely to one side, and search becomes O(n).

```
insert 1, 2, 3, 4, 5  ->   1
                            \
                             2
                              \
                               3
                                \
                                 ...
```

Real-world libraries use **self-balancing** variants (red-black trees,
AVL, B-trees on disk). We won't build a balanced one in this
curriculum — we'll just notice the problem on Day 90 and use it as
the punchline for "use a heap or a hash table or `sorted()` for
production code; reach for a BST when range queries matter."

## What you'll build today

A `BST` class wrapping a root pointer:

- `insert(x)` — duplicate-tolerant or set-semantics? You'll do set
  semantics (no duplicates).
- `contains(x)`
- `__iter__` — yields values in sorted order (inorder traversal).
- `min()` / `max()` — walk all the way left / all the way right.

## Now: open `fluency.py`

Two near-correct BST helpers, with the comparisons backwards.
