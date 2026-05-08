"""Rung 5: Apply.

Tiny CLI: a sorted-set REPL backed by your BST.

Commands:
    add <int>
    has <int>
    show           # ascending
    min / max
    quit

Try it:
    printf "add 5\\nadd 3\\nadd 7\\nshow\\nhas 4\\nmin\\nmax\\nquit\\n" \\
        | uv run python 05_apply.py
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_guided", Path(__file__).parent / "03_guided.py"
)
_guided = module_from_spec(_spec)
_spec.loader.exec_module(_guided)


def main() -> None:
    t = _guided.BST()
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        if line == "quit":
            return
        parts = line.split()
        if parts[0] == "add" and len(parts) == 2:
            t.insert(int(parts[1]))
        elif parts[0] == "has" and len(parts) == 2:
            print(int(parts[1]) in t)
        elif parts[0] == "show":
            print(", ".join(str(v) for v in t))
        elif parts[0] == "min":
            print(t.min())
        elif parts[0] == "max":
            print(t.max())
        else:
            print(f"unknown: {line!r}")


if __name__ == "__main__":
    main()
