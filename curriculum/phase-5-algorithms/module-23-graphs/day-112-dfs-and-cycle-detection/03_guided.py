"""Rung 3: Guided — count connected components in an UNDIRECTED graph.

Topic: classic DFS application.

Given an undirected graph as adjacency dict (so each edge appears in
both directions), return the number of connected components.

>>> count_components({1: [2], 2: [1], 3: [4], 4: [3], 5: []})
3
>>> count_components({})
0
>>> count_components({1: []})
1

Hints:
- Iterate every node. If unvisited, run DFS from it (mark every node
  it can reach as visited). That's one component.
- Repeat. The number of times you started a fresh DFS is the answer.
- Recursive or iterative DFS — your call.
"""


def count_components(adj: dict) -> int:
    raise NotImplementedError
