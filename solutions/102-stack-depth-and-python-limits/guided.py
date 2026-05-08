"""Rung 3: Guided — iterative DFS over a tree using an explicit stack.

Topic: replace recursion with a manual stack to escape the Python limit.

Implement `iter_keys(d)` that yields every dotted-path key in a nested
dict, using a *while* loop and an explicit list-as-stack. No recursion.

>>> sorted(iter_keys({"a": 1, "b": {"c": 2, "d": {"e": 3}}}))
['a', 'b.c', 'b.d.e']
>>> list(iter_keys({}))
[]

Hints:
- Stack starts as: [("", d)]   # (prefix, subtree)
- Loop: pop one off, look at it. If it's a dict, push each child onto
  the stack with the extended prefix. If it's a leaf value, yield the
  prefix.
- Order doesn't have to match recursion's order — tests sort the result.
"""


def iter_keys(d: dict):
    raise NotImplementedError
