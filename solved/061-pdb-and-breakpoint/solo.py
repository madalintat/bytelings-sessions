"""Rung 4: Solo implement — solved version.

Walk e.__traceback__ to the deepest frame, pull filename + lineno +
funcname from it, and format the one-line summary string.
os.path.basename gives just the filename without directory.
"""
import os
from typing import Any, Callable


def last_frame_summary(
    func: Callable, *args: Any, **kwargs: Any
) -> str | None:
    try:
        func(*args, **kwargs)
        return None
    except Exception as e:
        tb = e.__traceback__
        while tb.tb_next is not None:
            tb = tb.tb_next
        filename = os.path.basename(tb.tb_frame.f_code.co_filename)
        lineno = tb.tb_lineno
        funcname = tb.tb_frame.f_code.co_name
        return f"{type(e).__name__} at {filename}:{lineno} in {funcname}: {e}"
