"""Rung 3: Guided implement — solved version.

Walk the traceback chain (e.__traceback__) to the deepest frame,
then capture its f_locals snapshot. The "deepest frame" is the one
that actually raised; all prior frames are just the call path.
"""
import sys
import traceback
from typing import Any, Callable


def debug_call(func: Callable, *args: Any, **kwargs: Any) -> dict:
    """Call func(*args, **kwargs) and return a report dict."""
    try:
        result = func(*args, **kwargs)
        return {"status": "ok", "result": result}
    except Exception as e:
        # Walk to the deepest frame in the traceback.
        tb = e.__traceback__
        while tb.tb_next is not None:
            tb = tb.tb_next
        return {
            "status": "error",
            "error_type": type(e).__name__,
            "message": str(e),
            "frame_locals": dict(tb.tb_frame.f_locals),
        }
