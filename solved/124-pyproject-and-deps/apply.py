"""Rung 5: Apply — solved version.

Reads a pyproject.toml path from argv and prints a one-screen summary.
Reuses summarize_project from solo.py via dynamic import (same pattern
as the starter file — no change needed here beyond the stub being filled).

    uv run python apply.py path/to/pyproject.toml
"""
from __future__ import annotations

import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def main() -> None:
    if len(sys.argv) != 2:
        print("usage: python apply.py <path-to-pyproject.toml>")
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
