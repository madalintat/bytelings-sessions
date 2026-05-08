"""Rung 5: Apply.

Tiny REPL-ish loop. Pre-loaded catalog; user types `<isbn> <name>` to
check out a book. Domain errors print user-friendly messages instead
of tracebacks.

Try it:
  printf '111 bob\n222 carol\n999 dave\n' | uv run python 05_apply.py
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "04_solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    catalog = {
        "111": {"title": "Calculus", "borrower": None},
        "222": {"title": "SICP", "borrower": "alice"},
    }
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        try:
            isbn, name = line.split(maxsplit=1)
        except ValueError:
            print(f"input error: expected '<isbn> <name>', got {line!r}")
            continue
        try:
            rec = _solo.checkout(catalog, isbn, name)
            print(f"checked out '{rec['title']}' to {name}")
        except _solo.LibraryError as e:
            print(f"sorry: {e}")


if __name__ == "__main__":
    main()
