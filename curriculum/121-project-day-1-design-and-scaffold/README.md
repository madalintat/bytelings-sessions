---
day: 121-project-day-1-design-and-scaffold
phase: phase-5-algorithms
module: phase-5-project-pathfinder
style: story
---
# Day 121 — Day 1: design before code

You read the README. You know the goal. Before writing a single
solver, sketch the bones.

## Today's deliverable

Today you will:

1. Write a `parse_maze(text) -> Maze` that turns the ASCII grid into a
   structured object.
2. Write a `neighbors(maze, cell) -> Iterator[(neighbor, cost)]`
   function — the algorithms will all call this.
3. Stub `solve_bfs`, `solve_dfs`, `solve_dijkstra` so all three exist
   and raise `NotImplementedError`.
4. Get the parser tests green. The solver tests for tomorrow already
   exist but will fail today — that's expected.

## Design choices

**Cell type:** `tuple[int, int]` — `(row, col)`. Hashable, immutable,
fast.

**Maze type:** a small dataclass:

```python
@dataclass
class Maze:
    grid: list[list[str]]
    start: tuple[int, int]
    goal:  tuple[int, int]
    rows:  int
    cols:  int
```

**Neighbor function:** a single function the solvers all share. It
yields `(neighbor_cell, edge_cost)` tuples. For walls it yields
nothing. For digits `1`–`9` the cost is the digit; for `.`, `S`, `G`
the cost is 1.

This single design choice — neighbors-with-costs even when the cost
is uniform — lets the *same* function serve all three algorithms.
BFS and DFS will ignore the cost; Dijkstra will use it.

## The four directions

```python
DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))   # up, down, left, right
```

Pure aesthetics aside: keep this as a constant so the order is
deterministic (helpful when tests check path equality).

## Today's test target

The tests in `app_test.py` cover the parser and `neighbors` function.
The stub-solver tests just confirm `NotImplementedError` is raised —
the real solver tests live in tomorrow's folder.

## A small map of what tomorrow looks like

Day 122 will fill in the three solvers, all returning
`tuple[path, cost] | None`. Each one is short:

- BFS: ~15 lines, deque + parent dict.
- DFS: ~10 lines, recursion + path list.
- Dijkstra: ~20 lines, heap + dist dict.

If today's design is right, tomorrow is just plugging in the
algorithms.

## Now: open `app.py`

Implement the parser and neighbor function. Stub the three solvers.
Run `pytest app_test.py -k "parse or neighbors"` to focus on today's
tests.
