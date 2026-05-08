"""Rung 5: Apply.

Tiny CLI: read a pyproject.toml file path, print a one-screen summary.

    uv run python 05_apply.py path/to/pyproject.toml

Reuses summarize_project from rung 4. This is the same shape of tool
you'll write in tomorrow's `console_scripts` exercise — just one
function away from being installable as a real `pyproject-summary`
command.
"""
from __future__ import annotations
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "04_solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: python 05_apply.py <path-to-pyproject.toml>")
        sys.exit(1)
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"error: {path} not found")
        sys.exit(1)
    summary = _solo.summarize_project(path.read_text(encoding="utf-8"))
    print(f"{summary['name']} {summary['version']}")
    print(f"  python: {summary['python'] or '(any)'}")
    print(f"  deps ({len(summary['deps'])}): {', '.join(summary['deps']) or '(none)'}")
    print(f"  dev   ({len(summary['dev_deps'])}): {', '.join(summary['dev_deps']) or '(none)'}")


if __name__ == "__main__":
    main()
