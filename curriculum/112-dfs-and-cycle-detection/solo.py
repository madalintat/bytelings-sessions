"""Rung 4: Solo.

Topic: detect a cycle in a DIRECTED graph using DFS + 3-coloring.

Implement `has_cycle(adj)` that returns True iff the directed graph
has any cycle. Use the WHITE/GRAY/BLACK coloring described in the
concept page:
- WHITE: not yet visited.
- GRAY:  on the current DFS path.
- BLACK: fully explored, no cycle through here.

A cycle is detected when you find an edge to a GRAY node.

>>> has_cycle({1: [2], 2: [3], 3: []})
False
>>> has_cycle({1: [2], 2: [3], 3: [1]})
True
>>> has_cycle({1: [1]})    # self-loop counts
True

Tests in 04_solo_test.py are HIDDEN.
"""


def has_cycle(adj: dict) -> bool:
    raise NotImplementedError
