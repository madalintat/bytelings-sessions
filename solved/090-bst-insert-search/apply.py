"""Rung 5: Apply — solved version.

The apply has no TODO; once guided.py's BST class is implemented,
this REPL works. Identical to the starter (kept here so a learner
who deletes a line by accident can recover via `bytelings reset`).
"""
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location(
    "_guided", Path(__file__).parent / "guided.py"
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
