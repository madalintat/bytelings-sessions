"""Rung 5: Apply.

Mini "six degrees" demo: a tiny social graph, find the shortest path
between two people.

Try it: uv run python 05_apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "04_solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


FRIENDS = {
    "Bytelinger":   ["Anna", "Vlad"],
    "Anna":   ["Bytelinger", "Bea", "Tom"],
    "Vlad":   ["Bytelinger", "Tom"],
    "Bea":    ["Anna", "Sue"],
    "Tom":    ["Anna", "Vlad", "Carl"],
    "Sue":    ["Bea", "Carl"],
    "Carl":   ["Tom", "Sue"],
}


def main() -> None:
    pairs = [("Bytelinger", "Sue"), ("Bytelinger", "Carl"), ("Vlad", "Bea")]
    for a, b in pairs:
        path = _solo.shortest_path(FRIENDS, a, b)
        if path:
            print(f"{a} → {b}: {' → '.join(path)} ({len(path) - 1} hops)")
        else:
            print(f"{a} → {b}: not connected")


if __name__ == "__main__":
    main()
