---
day: day-087-binary-tree-basics
phase: phase-4-data-structures
module: module-18-trees-and-bst
style: metaphor
---
# Day 87 — A binary tree is a family tree

Picture a family. Every person has at most two children. Every person
has exactly one parent (except the very oldest ancestor, who has
none). You don't draw lines back from grandchildren to grandparents —
each generation only points down.

That's a **binary tree**. The "person" is a node; the children are
left and right; the oldest ancestor is the root. There's exactly one
path from the root to anyone in the tree. No loops, no shortcuts.

```
        root
        /  \
      [a]  [b]
      / \    \
    [c] [d]  [e]      <- leaves are nodes with no children
```

## The vocabulary you'll keep using

- **Root** — the top node. The whole tree is identified by it.
- **Leaf** — a node with no children.
- **Parent / child** — relative position; one step up or down.
- **Subtree** — any node, plus everything below it, is itself a tree.
- **Height** — longest root-to-leaf path, in *edges*. A single node
  has height 0. (Some texts say "in nodes" — when reading code,
  always check the convention.)
- **Depth** of a node — distance from the root, in edges. The root
  has depth 0.
- **Balanced** — informally, no leaf is far deeper than any other.
  We'll formalize this on Day 90.

## Why a tree, not a list?

A list is a one-dimensional sequence. A tree is *branching*: each
step gives you a choice. That branching is the magic. If you can
arrange data so each step *halves* the remaining work, you go from
O(n) to O(log n) — looking at 30 items instead of a billion. Trees
make this possible.

The classic shape that gets you the halving is the **binary search
tree**, which we'll build on Day 89. Today is just the skeleton: a
node with two children.

## In Python, it's almost too simple

```python
class TreeNode:
    __slots__ = ("value", "left", "right")
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

Three slots. That's it. The whole tree is just a root reference. The
recursion writes itself: anything you want to compute about a tree is
"do something to the root, then recurse into left and right."

## The recursive habit

For every tree algorithm, there are two questions:
1. **What's true at a leaf?** (the base case)
2. **How do I combine the answer for left and right?** (the recursive
   step)

`size(t) = 0 if t is None else 1 + size(t.left) + size(t.right)`.
`height(t) = -1 if t is None else 1 + max(height(t.left), height(t.right))`.
That's the whole pattern. Once you internalize it, every tree problem
melts down to "two questions."

## Now: open `fluency.py`

Two basic tree-shape helpers, each off by one in a recursive case.
