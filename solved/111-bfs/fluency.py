"""Rung 2: Fluency — solved version.

Mark a node visited at the MOMENT you enqueue it, not at pop time.
Otherwise multiple parents can each enqueue the same neighbor before
any of them gets popped, polluting the queue.

The clean shape: at every enqueue point, check `if nb not in visited`
and mark it visited atomically with the enqueue. The `if node in
visited: continue` guard at pop time becomes unnecessary.
"""
from collections import deque


def bfs_order(adj: dict, start) -> list:
    visited = {start}
    q = deque([start])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nb in adj.get(node, []):
            if nb not in visited:
                visited.add(nb)
                q.append(nb)
    return order
