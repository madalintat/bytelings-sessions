"""Rung 5: Apply.

Mini-CLI: read a list of paths from stdin, attempt to read each one,
print a one-line summary using classify_failure from rung 4.

Try it:
  printf '/etc/hosts\n/no/such/file\n' | uv run python apply.py
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        status, result = _solo.classify_failure(Path(line).read_text)
        if status == "ok":
            print(f"{line}: OK ({len(result)} bytes)")
        else:
            print(f"{line}: {status}")


if __name__ == "__main__":
    main()
