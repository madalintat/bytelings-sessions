"""Rung 4: Solo implement.

Topic: a tiny multi-command dispatcher

Build `dispatch(scripts, argv)`:

    scripts: dict[str, Callable[[list[str]], int]]
            Mapping of command name to handler. Each handler takes the
            remaining argv (everything after the command name) and
            returns an int exit code.
    argv:   list[str] — like sys.argv. argv[0] is the program name
            (ignored). argv[1] is the command name. argv[2:] are passed
            to the handler.

Behavior:
    - If argv has only the program name, print 'usage: <prog> <cmd>',
      list available commands sorted, and return 2.
    - If argv[1] is not in scripts, print 'unknown command: <name>'
      and return 2. Available commands listed, sorted.
    - Otherwise call the handler with argv[2:] and return its return value.

The print() calls must go to a `print` callable that takes one string;
default to the builtin. Tests will inject a fake to capture output.

Hidden tests live in 04_solo_test.py.
"""
from __future__ import annotations
from typing import Callable


def dispatch(
    scripts: dict[str, Callable[[list[str]], int]],
    argv: list[str],
    *,
    out=print,
) -> int:
    raise NotImplementedError
