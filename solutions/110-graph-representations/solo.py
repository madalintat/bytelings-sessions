"""Rung 4: Solo.

Topic: weighted directed graph.

Implement `build_weighted(edges)` where each edge is `(u, v, w)`
meaning "directed edge from u to v with weight w." Return an
adjacency dict mapping each node to a list of `(neighbor, weight)`
tuples.

>>> build_weighted([("a", "b", 5), ("a", "c", 2), ("b", "c", 1)])
{'a': [('b', 5), ('c', 2)], 'b': [('c', 1)]}

(Order of neighbors should follow insertion order — i.e., the order
they appear in `edges`.)

Also implement `total_weight(adj)`: return the sum of all edge
weights in the graph (each directed edge once).

>>> total_weight({'a': [('b', 5)], 'b': [('c', 1)]})
6

Tests in 04_solo_test.py are HIDDEN.
"""


def build_weighted(edges: list[tuple]) -> dict:
    raise NotImplementedError


def total_weight(adj: dict) -> int:
    raise NotImplementedError
