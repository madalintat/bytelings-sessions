"""Rung 5: Apply.

A real-feeling lint command:

    uv run python 05_apply.py path/to/file.py [path/to/another.py ...]

Prints one line per issue:

    path/to/file.py:12: M001 mutable default in foo

Exit code: 0 if no issues, 1 if any.

This is the same output format `flake8` and `ruff` use, which means
your editor's "jump to next problem" already groks it.
"""
from __future__ import annotations
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_HERE = Path(__file__).parent
_s = spec_from_file_location("_d127_solo", _HERE / "04_solo.py")
_solo = module_from_spec(_s)
sys.modules["_d127_solo"] = _solo
_s.loader.exec_module(_solo)


def main() -> int:
    paths = sys.argv[1:]
    if not paths:
        print("usage: python 05_apply.py <file.py> [file.py ...]")
        return 1
    found = 0
    for p in paths:
        path = Path(p)
        if not path.is_file():
            print(f"{p}: not a file", file=sys.stderr)
            found += 1
            continue
        src = path.read_text(encoding="utf-8")
        for issue in _solo.lint(src):
            print(f"{p}:{issue.line}: {issue.code} {issue.message}")
            found += 1
    return 0 if found == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
