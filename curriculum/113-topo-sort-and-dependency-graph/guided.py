"""Rung 3: Guided — topo sort with cycle detection.

Topic: practical topological sort that fails loudly on cycles.

Implement `build_order(deps)` where `deps` is a list of (prereq,
dependent) pairs meaning "prereq must come before dependent."

Return a list giving a valid build order of every package mentioned.
If there's a cycle, raise ValueError("cycle detected").

>>> build_order([("shared", "frontend"), ("shared", "backend")])
# any order with 'shared' first
>>> build_order([("a", "b"), ("b", "a")])
ValueError: cycle detected

Hints:
- Build adjacency dict from deps. Make sure every package appears as
  a key (use indeg.setdefault or similar).
- Use Kahn's algorithm.
- Detect cycle by comparing len(out) vs len(all packages).
"""


def build_order(deps: list[tuple]) -> list:
    raise NotImplementedError
