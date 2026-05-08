"""Rung 4: Solo implement.

Topic: post-mortem analysis using sys.exc_info / traceback walking.

Implement `last_frame_summary(func, *args, **kwargs) -> str | None`:

  - Call func(*args, **kwargs).
  - On success, return None.
  - On exception, return a string formatted exactly like:
        "<error_type> at <filename>:<lineno> in <funcname>: <message>"
    where the location is the *deepest* frame in the traceback (the
    actual line that raised), `<filename>` is the basename only, and
    `<message>` is str(exception).

  Examples:
    last_frame_summary(lambda: None)              -> None
    last_frame_summary(lambda: 1/0)               -> "ZeroDivisionError at solo.py:NN in <lambda>: division by zero"

Hidden tests in 04_solo_test.py.
"""
from typing import Any, Callable


def last_frame_summary(
    func: Callable, *args: Any, **kwargs: Any
) -> str | None:
    raise NotImplementedError
