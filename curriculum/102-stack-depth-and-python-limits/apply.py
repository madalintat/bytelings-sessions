"""Rung 5: Apply.

Compare a recursive walker (which crashes) against the explicit-stack
walker (which doesn't), on a 2000-deep tree. Reproduces yesterday's
detective scene.

Try it: uv run python apply.py
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def build_deep_tree(depth: int) -> dict:
    cur = {"value": 0, "children": []}
    for i in range(1, depth):
        cur = {"value": i, "children": [cur]}
    return cur


def rec_max(node):
    best = node["value"]
    for c in node["children"]:
        cm = rec_max(c)
        if cm > best:
            best = cm
    return best


def main() -> None:
    sys.setrecursionlimit(1000)
    tree = build_deep_tree(2000)

    try:
        print(f"recursive max: {rec_max(tree)}")
    except RecursionError:
        print("recursive max: RecursionError (depth > 1000)")

    print(f"iterative max: {_solo.max_value(tree)}  (no crash)")


if __name__ == "__main__":
    main()
