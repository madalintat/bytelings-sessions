"""Rung 3: Guided — solved version.

iter_keys uses an explicit list as a stack. Each entry is (prefix, subtree).
When we pop a non-dict value, yield the prefix. When we pop a dict,
push each (child_prefix, child_subtree) pair. No recursion, so depth
is only bounded by the stack size in memory — no recursion limit.
"""


def iter_keys(d: dict):
    """Yield every dotted-path key in a nested dict. Iterative DFS.

    >>> sorted(iter_keys({"a": 1, "b": {"c": 2, "d": {"e": 3}}}))
    ['a', 'b.c', 'b.d.e']
    """
    stack = [("", d)]
    while stack:
        prefix, subtree = stack.pop()
        if not isinstance(subtree, dict):
            yield prefix
        else:
            for k, v in subtree.items():
                child_prefix = f"{prefix}.{k}" if prefix else k
                stack.append((child_prefix, v))
