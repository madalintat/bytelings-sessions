"""Rung 5: Apply.

Tiny CLI: read words from stdin (whitespace-separated), print anagram
groups, one group per line, words space-separated within a group.

Reuses anagram_groups from rung 4.

Try it: echo "eat tea tan ate nat bat" | uv run python apply.py

Patterns: P-07 (accumulator-into-dict), P-10 (visit-set-for-dedup).
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_solo", Path(__file__).parent / "solo.py"
)
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    words = sys.stdin.read().split()
    for group in _solo.anagram_groups(words):
        print(" ".join(group))


if __name__ == "__main__":
    main()
