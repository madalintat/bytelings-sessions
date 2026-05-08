"""Rung 5: Apply.

Tiny CLI: read two files (paths via argv), interleave their lines.

Reuses interleave from rung 4.

Try it:
  echo -e "1\\n2\\n3" > /tmp/a.txt
  echo -e "a\\nb"     > /tmp/b.txt
  uv run python apply.py /tmp/a.txt /tmp/b.txt
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
    if len(sys.argv) != 3:
        print("usage: apply.py <file_a> <file_b>", file=sys.stderr)
        sys.exit(2)
    a_lines = Path(sys.argv[1]).read_text().splitlines()
    b_lines = Path(sys.argv[2]).read_text().splitlines()
    for line in _solo.interleave(a_lines, b_lines):
        print(line)


if __name__ == "__main__":
    main()
