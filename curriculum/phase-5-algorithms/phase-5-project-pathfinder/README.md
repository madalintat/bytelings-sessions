# Phase 5 Project — Pathfinder

A small CLI that finds paths through 2D grid mazes using BFS, DFS, and
Dijkstra. By the end of three days, you'll have a working tool that
reads an ASCII maze, picks an algorithm, and prints the path on top
of the grid.

## The Scenario

You're prototyping the navigation core for a tiny robot that must
navigate warehouse aisles. The aisles are an ASCII grid:

```text
S....#....
.###.#....
.#...#....
.#.###.###
.#.....#.G
######.#..
.......#..
##########
```

- `S` — start cell
- `G` — goal cell
- `#` — wall (impassable)
- `.` — open floor (cost 1)
- digits `1`–`9` — open floor with that movement cost (Dijkstra only)

Move up/down/left/right (no diagonals). The robot needs the
*shortest* route under different cost models.

## Requirements

The shipping CLI must:

1. Read a maze from a text file (or stdin).
2. Accept a `--algo` flag: `bfs`, `dfs`, or `dijkstra`.
3. Print the maze with the path overlaid in `*` characters between
   `S` and `G` (exclusive of both).
4. Print the total path cost (length for BFS/DFS, weighted sum for
   Dijkstra).
5. Print "no path found" cleanly if the goal is unreachable.

## Concepts checklist (this phase, exercised here)

- [x] Recursion / iteration choice (DFS — recursion or explicit stack).
- [x] Adjacency representations (we use coordinate tuples + neighbor
      function rather than a built dict).
- [x] BFS — shortest path in unweighted graphs.
- [x] DFS — visit-every-cell, *not* shortest path; teaches the
      contrast.
- [x] Heaps (Module 19) — Dijkstra needs a priority queue.
- [x] DP-flavored shortest paths — Dijkstra is "best-known cost so
      far" tabulation.
- [x] Tests with pytest (Phase 3).
- [x] CLI design + `argparse` (touches packaging concerns from later).

## Day-by-day plan

**Day 121 — Design and scaffold.**
Choose your data model. Write the maze parser. Define the neighbor
function. Stub the three solvers. Get one happy-path test green.

**Day 122 — Build the core.**
Implement BFS, DFS, and Dijkstra. Add path reconstruction. Make all
three return `(path, cost)` or `None`. Most of the day is here.

**Day 123 — Test and ship.**
Edge cases: no path, S adjacent to G, weighted maze where Dijkstra
beats BFS. Pretty-print the overlaid path. Wrap in argparse. Smoke
test on a few mazes.

## Graduated hints

<details>
<summary>Stuck on the data model?</summary>

Use `(row, col)` tuples as nodes. The maze is `list[list[str]]`. The
neighbor function takes `(r, c)` and yields `(nr, nc)` for each
of the 4 directions, skipping out-of-bounds and walls.

</details>

<details>
<summary>How do I reconstruct the path from BFS?</summary>

Maintain a `parent: dict[Cell, Cell]` during BFS. After the BFS loop,
walk parent[goal] → parent[parent[goal]] → ... → start, then reverse.

</details>

<details>
<summary>Dijkstra hint</summary>

Use `heapq`. Push `(cost_so_far, cell)`. On pop, if the cell's been
finalized (cost in `dist` already and current pop's cost is higher),
skip. Otherwise relax each neighbor.

</details>

## Stretch goals (optional)

- A* with a Manhattan-distance heuristic. Compare expansion counts
  vs Dijkstra on the same maze.
- Animated terminal output: print each step of BFS expanding.
- A maze generator using recursive backtracking (Module 24).
- Read GIF/PNG mazes (color thresholds).

## Self-evaluation rubric (before declaring done)

- [ ] BFS finds the same shortest length as a hand-counted answer on
      a 5×5 maze.
- [ ] DFS finds *a* path on the same maze, but you can articulate
      why DFS doesn't promise shortest.
- [ ] Dijkstra finds the cost-cheapest path on a maze with `2`s in
      the way of the BFS-shortest, and it differs from BFS's.
- [ ] All three return `None` (or equivalent) when no path exists.
- [ ] CLI reads a file, prints the path overlay and total cost.
- [ ] You can explain — without notes — why BFS gives shortest
      hop-count and Dijkstra gives shortest weighted cost.
