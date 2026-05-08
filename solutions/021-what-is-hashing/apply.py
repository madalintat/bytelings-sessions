"""Rung 5: Apply.

Tiny CLI: read words from stdin (one per line), print each unique word
exactly once, in first-seen order, using TinySet for membership.

Reuses TinySet from rung 4.

Try it: printf "a\nb\na\nc\nb\n" | uv run python apply.py
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
    seen = _solo.TinySet()
    for line in sys.stdin:
        word = line.rstrip("\n")
        if word in seen:
            continue
        seen.add(word)
        print(word)


if __name__ == "__main__":
    main()
