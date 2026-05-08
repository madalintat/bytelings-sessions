---
day: 110-graph-representations
phase: phase-5-algorithms
module: module-23-graphs
style: compare
---
# Day 110 — Two ways to store a graph. Pick wisely.

You have to model a social network: users, who follows whom. There are
two structurally different ways to store this in memory, and the wrong
choice will silently destroy your performance.

## Way A — adjacency matrix

```python
n = 5
adj = [[0] * n for _ in range(n)]   # n×n grid of 0s
adj[0][1] = 1                       # 0 follows 1
adj[2][3] = 1                       # 2 follows 3
```

A 2D grid where `adj[u][v] == 1` means "edge from u to v." Pretty
much how a math textbook draws it.

**Strengths.** Constant-time edge lookup: "does u follow v?" → one
indexing op. Easy to reason about.

**Weakness.** O(n²) memory, *regardless of how many edges exist*.
For 1 million users with sparse follow patterns, that's a 10^12-cell
matrix. You don't have that RAM. Don't try.

## Way B — adjacency list

```python
adj = {0: [1], 2: [3]}
# OR a list of lists, indexed by node:
# adj = [[1], [], [3], [], []]
```

A dict-of-lists (or list-of-lists). Each node maps to its neighbors.

**Strengths.** O(V + E) memory — pay only for actual edges. Iterating
"all neighbors of u" is a direct list walk: O(deg(u)). For sparse
real-world graphs, this is what you want 99% of the time.

**Weakness.** "Does u follow v?" is now O(deg(u)) — you have to scan
u's neighbor list. (Mitigation: store neighbors as sets for O(1)
membership at the cost of slightly higher constant factors.)

## The decision rule

| Property | Matrix | List |
|---|---|---|
| Memory | O(n²) | O(n + e) |
| "Edge u→v exists?" | O(1) | O(deg) |
| "All neighbors of u?" | O(n) | O(deg) |
| Adding an edge | O(1) | O(1) amortized |
| Sparse graphs | terrible | great |
| Dense graphs (e ≈ n²) | great | fine |

Pick **list** for almost everything. Real-world graphs (social
networks, web pages, road maps) are *sparse*: a node has tens of
neighbors, not millions. Adjacency lists save memory by orders of
magnitude.

Pick **matrix** when:

- The graph is small AND dense (n ≤ a few hundred, edges fill most
  of the matrix).
- You need many "is there an edge u→v?" checks.
- Floyd-Warshall or other matrix-based algorithms (out of scope).

## Directed vs undirected; weighted vs unweighted

Two more dimensions to know:

- **Directed:** edges have direction (u → v ≠ v → u). Twitter
  follows. Web links. Use them when "A points to B" and "B points
  to A" are different facts.
- **Undirected:** edges go both ways (Facebook friendships, road
  segments). Just store both directions in your representation.
- **Weighted:** edges carry a number (distance, cost, duration). For
  adjacency lists, store `(neighbor, weight)` tuples. Required for
  Dijkstra (PP5).

In Python, the cleanest representation for almost all real work:

```python
adj: dict[Node, list[Node]] = defaultdict(list)
# or for weighted:
adj: dict[Node, list[tuple[Node, int]]] = defaultdict(list)
```

## WHEN this matters

Every algorithm in this module — BFS, DFS, topological sort,
Dijkstra (PP5) — runs on top of one of these representations. The
algorithm is the same; the cost depends entirely on which storage you
chose. Get this right today and the rest of the module is downhill.

## Now: open `fluency.py`

A function builds an adjacency list but forgets to make undirected
edges go both ways. Fix it.
