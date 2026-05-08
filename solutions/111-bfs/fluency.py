"""Rung 2: Fluency drill — fix the BFS visit-order.

Topic: BFS with a queue + visited set.

`bfs_order` is supposed to return the nodes in BFS order from `start`.
The check `if nb not in visited` is in the wrong place: it adds
duplicates to the queue, then "fixes" them later, which produces the
wrong order on graphs with multiple paths to the same node.

Move the visited-add to happen at the moment a neighbor is enqueued.
"""
from collections import deque


def bfs_order(adj: dict, start) -> list:
    visited = set()
    q = deque([start])
    order = []
    while q:
        node = q.popleft()
        if node in visited:
            continue       # TODO: remove this line and fix the issue properly
        visited.add(node)  # TODO: too late — duplicates already in the queue
        order.append(node)
        for nb in adj.get(node, []):
            q.append(nb)   # TODO: only add if not visited yet
    return order
