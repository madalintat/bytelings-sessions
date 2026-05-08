"""Rung 4: Solo implement — solved version.

`dispatch` is a tiny command dispatcher:
- No argv[1]  → print usage + sorted command list, return 2.
- Unknown cmd → print error + sorted command list, return 2.
- Known cmd   → delegate to handler(argv[2:]), return its code.

The `out` parameter (defaulting to `print`) is injected in tests to
capture output without monkeypatching builtins.
"""
from __future__ import annotations

from typing import Callable


def dispatch(
    scripts: dict[str, Callable[[list[str]], int]],
    argv: list[str],
    *,
    out=print,
) -> int:
    """Dispatch argv to the matching handler in scripts.

    Returns the handler's return code, or 2 on usage/unknown-command error.
    """
    prog = argv[0] if argv else "prog"
    available = sorted(scripts)

    if len(argv) < 2:
        out(f"usage: {prog} <cmd>")
        out("available commands: " + ", ".join(available))
        return 2

    cmd = argv[1]
    if cmd not in scripts:
        out(f"unknown command: {cmd}")
        out("available commands: " + ", ".join(available))
        return 2

    return scripts[cmd](argv[2:])
