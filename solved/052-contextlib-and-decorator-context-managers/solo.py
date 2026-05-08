"""Rung 4: Solo — solved version.

`ExitStack` acts as a dynamic `with` manager: `stack.enter_context(f)`
registers the file handle so it is closed when the stack exits — even
if an earlier open fails. We strip trailing newlines with `rstrip("\\n")`
to match the spec.
"""
from contextlib import ExitStack


def read_all_lines(paths: list) -> list[str]:
    if not paths:
        return []
    lines: list[str] = []
    with ExitStack() as stack:
        for path in paths:
            f = stack.enter_context(open(path, encoding="utf-8"))
            for line in f:
                lines.append(line.rstrip("\n"))
    return lines
