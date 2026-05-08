"""Rung 5: Apply.

Build a tiny package-build planner. Given a list of (prereq, dep)
pairs, print the order you'd run them. Bail loudly on cycles.

Try it: uv run python apply.py

Patterns: P-07 (accumulator-into-dict), P-27 (dfs-with-explicit-stack).
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    courses = [
        (1, 0),  # course 1 needs course 0
        (2, 1),
        (3, 2),
        (4, 1),
        (5, 4),
    ]
    print(f"can finish 6 courses with prereqs? {_solo.can_finish(6, courses)}")

    impossible = courses + [(0, 5)]   # introduce a cycle
    print(f"with cycle added? {_solo.can_finish(6, impossible)}")


if __name__ == "__main__":
    main()
