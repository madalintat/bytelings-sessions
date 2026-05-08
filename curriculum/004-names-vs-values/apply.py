"""Rung 5 — dedupe lines from stdin in order of first appearance.

Try: printf "a\\nb\\na\\nc\\nb\\n" | uv run python apply.py
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
    lines = [ln.rstrip("\n") for ln in sys.stdin]
    for ln in _solo.unique_preserving_order(lines):
        print(ln)


if __name__ == "__main__":
    main()
