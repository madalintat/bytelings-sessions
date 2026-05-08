"""Rung 5: Apply — solved version.

Apply has no TODO; once solo.py's `can_finish` is in, the
package-build-planner demo runs.
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
        (1, 0),
        (2, 1),
        (3, 2),
        (4, 1),
        (5, 4),
    ]
    print(f"can finish 6 courses with prereqs? {_solo.can_finish(6, courses)}")

    impossible = courses + [(0, 5)]
    print(f"with cycle added? {_solo.can_finish(6, impossible)}")


if __name__ == "__main__":
    main()
