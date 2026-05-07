"""Rung 3: Guided — convert between matrix and adjacency list.

Topic: two representations of the same graph.

Implement two converters:

`matrix_to_adj(m)`: given an n×n 0/1 matrix where m[i][j] == 1 means
"edge i → j", return an adjacency dict {i: [neighbors]}. Treat the
graph as DIRECTED (don't add reverse edges).

`adj_to_matrix(adj, n)`: given an adjacency dict and the number of
nodes n, return an n×n 0/1 matrix.

>>> matrix_to_adj([[0,1,0],[0,0,1],[1,0,0]])
{0: [1], 1: [2], 2: [0]}
>>> adj_to_matrix({0: [1], 1: [2], 2: [0]}, 3)
[[0, 1, 0], [0, 0, 1], [1, 0, 0]]

Hints:
- Iterate row by row; collect indices where the cell is 1.
- For adj_to_matrix, start with an n×n zero matrix and flip cells.
- Nodes with no out-edges should still appear in the dict (with empty
  list) when converting from matrix.
"""


def matrix_to_adj(m: list[list[int]]) -> dict[int, list[int]]:
    raise NotImplementedError


def adj_to_matrix(adj: dict[int, list[int]], n: int) -> list[list[int]]:
    raise NotImplementedError
