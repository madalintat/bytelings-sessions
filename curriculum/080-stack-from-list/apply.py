"""Rung 5: Apply.

Tiny CLI: an undo-stack for a single text buffer.

Read commands from stdin, one per line:
    set <text>     replace the buffer with <text> (snapshot first)
    undo           pop the last snapshot
    show           print the current buffer
    quit           stop

Run it:
    printf "set hello\\nset world\\nundo\\nshow\\nquit\\n" | uv run python 05_apply.py
    -> hello
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
    history: _guided.Stack = _guided.Stack()
    buffer = ""
    for raw in sys.stdin:
        line = raw.rstrip("\n")
        if not line:
            continue
        if line == "quit":
            return
        if line == "show":
            print(buffer)
        elif line == "undo":
            if history:
                buffer = history.pop()
            else:
                print("(nothing to undo)")
        elif line.startswith("set "):
            history.push(buffer)
            buffer = line[len("set "):]
        else:
            print(f"unknown: {line!r}")


if __name__ == "__main__":
    main()
