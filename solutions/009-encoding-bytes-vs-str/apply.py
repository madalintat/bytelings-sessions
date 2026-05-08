"""Rung 5: Apply.

Tiny CLI: read raw bytes from stdin, print the character count under
each encoding (utf-8, latin-1).

Reuses count_chars from rung 4.

Try it: printf "café" | uv run python apply.py
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
    raw = sys.stdin.buffer.read()
    print(f"bytes:    {len(raw)}")
    print(f"utf-8:    {_solo.count_chars(raw, encoding='utf-8')}")
    print(f"latin-1:  {_solo.count_chars(raw, encoding='latin-1')}")


if __name__ == "__main__":
    main()
