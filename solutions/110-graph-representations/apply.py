"""Rung 5: Apply.

Build a tiny city-distances graph as an adjacency list and print a
summary. This is the same shape Dijkstra will use in PP5.

Try it: uv run python apply.py

Patterns: P-10 (visit-set-for-dedup), P-27 (dfs-with-explicit-stack).
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    edges = [
        ("Cluj", "Bucharest", 450),
        ("Cluj", "Oradea", 150),
        ("Cluj", "Iasi", 380),
        ("Bucharest", "Constanta", 220),
        ("Iasi", "Bucharest", 410),
    ]
    adj = _solo.build_weighted(edges)

    print("City graph (adjacency list):")
    for city, links in adj.items():
        for nb, w in links:
            print(f"  {city:>10}  --{w} km-->  {nb}")
    print(f"\nTotal road length: {_solo.total_weight(adj)} km")


if __name__ == "__main__":
    main()
