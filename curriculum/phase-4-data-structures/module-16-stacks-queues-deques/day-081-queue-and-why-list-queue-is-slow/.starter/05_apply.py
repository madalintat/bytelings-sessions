"""Rung 5: Apply.

Tiny CLI: a fair-share task scheduler.

Stdin lines look like:
    add <task>      enqueue a task
    next            dequeue and print the next task
    show            print the queue contents (front to back)
    quit            stop

Try it:
    printf "add print-doc\\nadd email-bob\\nnext\\nshow\\nquit\\n" | uv run python 05_apply.py
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
    q: _guided.Queue = _guided.Queue()
    for raw in sys.stdin:
        line = raw.rstrip("\n")
        if not line:
            continue
        if line == "quit":
            return
        if line == "next":
            if q:
                print(q.dequeue())
            else:
                print("(empty)")
        elif line == "show":
            # peek into the deque inside the Queue: walk via dequeue
            # into a temp list, then put them back. Naive but clear.
            items = []
            while q:
                items.append(q.dequeue())
            for x in items:
                q.enqueue(x)
            print(" -> ".join(items) if items else "(empty)")
        elif line.startswith("add "):
            q.enqueue(line[len("add "):])
        else:
            print(f"unknown: {line!r}")


if __name__ == "__main__":
    main()
