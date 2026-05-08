---
day: 088-tree-traversals
phase: phase-4-data-structures
module: module-18-trees-recursion-bst
style: trace
---
# Day 88 — Trace this: which traversal gives which order?

Look at this tree. It's the same one for the rest of the page.

```
        4
       / \
      2   6
     / \   \
    1   3   7
```

Predict each line *before* you scroll.

```python
preorder(root)    # ?
inorder(root)     # ?
postorder(root)   # ?
levelorder(root)  # ?
```

The answers:

```text
preorder    -> [4, 2, 1, 3, 6, 7]
inorder     -> [1, 2, 3, 4, 6, 7]
postorder   -> [1, 3, 2, 7, 6, 4]
levelorder  -> [4, 2, 6, 1, 3, 7]
```

The names tell you exactly when the **node itself** is visited
relative to its children. Pre = before children. In = between left
and right. Post = after both children. The recursion is identical;
only the placement of `visit(node)` moves.

## The three depth-first traversals

```python
def preorder(node, out):
    if node is None: return
    out.append(node.value)        # visit FIRST
    preorder(node.left, out)
    preorder(node.right, out)

def inorder(node, out):
    if node is None: return
    inorder(node.left, out)
    out.append(node.value)        # visit BETWEEN
    inorder(node.right, out)

def postorder(node, out):
    if node is None: return
    postorder(node.left, out)
    postorder(node.right, out)
    out.append(node.value)        # visit LAST
```

Three identical skeletons; one line moves. Memorize the *positions*,
not the answers.

## Why each one matters

- **Preorder** is the natural shape of "do this to a node, then to
  each child" — copying a tree, serializing one, walking a directory.
- **Inorder** on a *binary search tree* visits values in sorted
  order. That's why BSTs feel useful — inorder = sorted scan.
- **Postorder** processes children first, parent last — perfect for
  freeing memory, computing sizes, summing subtrees, evaluating
  expression trees from the leaves up.

## The fourth: level-order (BFS)

DFS uses recursion, which is implicitly a *stack*. Level-order goes
across the tree one row at a time and uses an explicit *queue*:

```python
from collections import deque

def levelorder(root):
    if root is None: return []
    q, out = deque([root]), []
    while q:
        node = q.popleft()
        out.append(node.value)
        if node.left:  q.append(node.left)
        if node.right: q.append(node.right)
    return out
```

The pattern flip — recursive (stack) for DFS, iterative + deque for
BFS — is the canonical move. You'll reuse the same shape on graphs in
Phase 5.

## The trick to remember

| Order | Where `visit` lives | Implementation |
|---|---|---|
| pre  | before recursion | recursion |
| in   | between recursions | recursion |
| post | after recursion | recursion |
| level| - | iterative + queue |

That's the whole conceptual cost. After this day, every "walk a tree
and do X" problem reduces to "which order, and what's X."

## Now: open `fluency.py`

Two traversals are mislabeled. Fix the line that moves.
