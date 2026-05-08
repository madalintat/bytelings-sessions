"""Rung 5: Apply.

Tiny CLI: read names from stdin (one per line), print an English list.

Reuses english_list from rung 4.

Try it: printf "alice\nbob\ncarol\n" | uv run python apply.py
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
    names = [line.strip() for line in sys.stdin if line.strip()]
    print(_solo.english_list(names))


if __name__ == "__main__":
    main()
