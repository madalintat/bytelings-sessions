---
day: day-123-project-day-3-test-and-ship
phase: phase-5-algorithms
module: phase-5-project-pathfinder
style: story
---
# Day 123 — Day 3: ship the CLI

Both the parser and the three solvers work. Time to wrap them in a
CLI a human can actually use, and to harden the edge cases.

## Today's deliverables

1. **`render_path(maze, path)`** — overlay the path on the grid as
   `*` characters (excluding S and G), return the multi-line string.
2. **`run_cli(args)`** — accept an algorithm name and a maze string;
   return the rendered output and a status line ("path found, cost=…"
   or "no path").
3. **`if __name__ == '__main__'`** — argparse-driven, reads from a
   file or stdin, prints to stdout. (Tests don't exercise this — they
   exercise `run_cli` directly. The argparse part is for you to use.)
4. **More tests** — bigger mazes, S adjacent to G, S == G.

## The render function

```python
def render_path(maze, path):
    grid = [row[:] for row in maze.grid]    # deep-ish copy
    for r, c in path:
        if grid[r][c] not in ("S", "G"):
            grid[r][c] = "*"
    return "\n".join("".join(row) for row in grid)
```

Every `*` is a step on the path. S and G stay readable.

## The run_cli function

```python
def run_cli(algo: str, maze_text: str) -> tuple[str, str]:
    maze = parse_maze(maze_text)
    solvers = {"bfs": solve_bfs, "dfs": solve_dfs, "dijkstra": solve_dijkstra}
    if algo not in solvers:
        return ("", f"unknown algorithm: {algo}")
    result = solvers[algo](maze)
    if result is None:
        return (maze_text.rstrip(), "no path found")
    path, cost = result
    rendered = render_path(maze, path)
    return (rendered, f"path found, cost={cost}, length={len(path)}")
```

Returning a tuple `(grid_text, status)` keeps the function
testable — the argparse layer wraps and prints them.

## The argparse layer

Eight lines, no surprises:

```python
import argparse, sys

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--algo", default="bfs", choices=("bfs", "dfs", "dijkstra"))
    p.add_argument("file", nargs="?", default="-")
    args = p.parse_args()
    text = sys.stdin.read() if args.file == "-" else open(args.file).read()
    rendered, status = run_cli(args.algo, text)
    print(rendered)
    print(status)

if __name__ == "__main__":
    main()
```

## What good edge-case testing looks like

You've already tested:
- Tiny mazes
- Wall blocks
- Weighted paths

Edge cases to add today:

1. **S equals G.** The path is just `[S]` and cost is 0. Easy to
   forget; easy to break.
2. **S adjacent to G.** Two-cell path, cost 1.
3. **Maze with no walls but a "trap" U-shape that DFS will follow
   wrong way.** Confirms DFS doesn't promise shortest.
4. **Maze with cheap detour.** Confirms Dijkstra differs from BFS.
5. **Render a non-trivial path** and check the resulting string has
   the right number of `*` characters.

## A reflection question

Before you call this done: open `progress/notes/day-123.md` (or just
on paper) and answer:

- *When would I reach for BFS in real code, not in a class?*
- *When would DFS be the right call, even though it's not shortest?*
- *Why does Dijkstra need non-negative weights?*

Real-world recognition is the goal of this whole module. If you can
answer those three questions in your own words, you've got it.

## Now: open `app.py`

Most code is filled in for you (parser, neighbors, solvers from
yesterday). Today, write `render_path` and `run_cli`, and make the
new tests green.
