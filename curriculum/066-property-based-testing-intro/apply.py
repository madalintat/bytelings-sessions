"""Rung 5: Apply.

Use `merge_sorted` from rung 4 to merge a list of pre-sorted streams
(simulating, e.g., merging sorted log files) into one sorted output.

Try it: uv run python apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from functools import reduce
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def merge_all(streams: list[list[int]]) -> list[int]:
    """Merge any number of sorted streams via repeated pairwise merge."""
    return reduce(_solo.merge_sorted, streams, [])


def main() -> None:
    streams = [
        [1, 4, 7, 10],
        [2, 5, 8, 11],
        [3, 6, 9, 12],
    ]
    print(merge_all(streams))


if __name__ == "__main__":
    main()
