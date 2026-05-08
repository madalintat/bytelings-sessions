---
day: day-090-bst-delete-and-balance
phase: phase-4-data-structures
module: module-18-trees-and-bst
style: detective
---
# Day 90 — Delete is a crime scene

You wrote a BST yesterday. Insert was clean. Search was clean. Today
you write **delete**, and you'll find out why every textbook spends
twice as many pages on it.

The crime: you've been asked to remove value 50 from this tree.

```
            50
           /  \
         30    70
        /  \   / \
       20  40 60 80
```

You remove the node. Now there's a hole at the root. The two
subtrees `30` and `70` are orphans. You can't just put one of them
on top — the BST invariant gets violated either way:

- Promote 30? But 70's whole subtree is bigger than 50, which is
  bigger than 30 — so 70 ends up on the *left* side. Nope.
- Promote 70? Now 30 hangs off 70 on the left, but 60 needs to fit
  *between* 30 and 70 in the left subtree of 70. That means 60 has to
  move. Half the tree just rearranged itself.

There's a third option, and it's the right one.

## The clue: in-order successor

The "next" value after 50 in sorted order is 60 — the leftmost node
of the right subtree. By definition, 60 is *smaller than everything
to the right of 50* and *larger than everything to the left of 50*
(except 50 itself). It's the only value that can stand in for 50
without breaking anything.

So the procedure for deleting a node N with two children:
1. Find N's **in-order successor** S (smallest value in N's right
   subtree).
2. Copy S.value into N.
3. Delete the original S from N's right subtree (S has at most one
   child — recursive case is now easy).

For nodes with 0 or 1 child, deletion is straightforward:
- **Leaf** — just remove it.
- **One child** — splice the child up to take the parent's place.

That's three cases. Two are easy. The third (two-children) is the
clue, and the in-order successor is the alibi.

## The pattern

```python
def delete(root, x):
    if root is None: return None
    if x < root.value:
        root.left = delete(root.left, x)
    elif x > root.value:
        root.right = delete(root.right, x)
    else:                                  # found it
        if root.left is None:  return root.right
        if root.right is None: return root.left
        # two children: copy successor's value, recurse on right
        succ = _min_node(root.right)
        root.value = succ.value
        root.right = delete(root.right, succ.value)
    return root
```

Like insert, delete returns the (maybe new) subtree root and the
caller assigns it back. That handles the "replaced by a child"
splice without a special case.

## The bigger crime: the BST might be skewed

If you insert sorted values into a BST, you build a chain. A million
inserts, then a `contains`, can take a million comparisons — O(n).
Production code uses **self-balancing** BSTs (red-black, AVL,
B-trees) to enforce O(log n) regardless of insertion order. We
won't build one in this curriculum.

But you should know the symptom: if you ever profile a "tree-backed"
data structure and find one operation is suspiciously slow, the first
thing to ask is *is the tree skewed?* You can measure it: compare
height to log2(size). If they're far apart, you've got a chain
masquerading as a tree.

## Today's brief

- Implement `delete(x)` on yesterday's BST, all three cases.
- Write a tiny `is_balanced` and `height` so you can *spot* a chain.
- Apply: a CLI that loads numbers and reports whether the resulting
  tree is healthy or skewed.

## Now: open `fluency.py`

Two delete attempts; each fails on a different case.
