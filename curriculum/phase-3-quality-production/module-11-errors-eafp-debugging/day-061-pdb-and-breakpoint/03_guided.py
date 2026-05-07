"""Rung 3: Guided implement — build a debug helper that mimics what
a pdb session gives you.

Topic: post-mortem inspection without an interactive prompt.

Real-world framing: in production you can't drop into pdb on a live
process. The next-best thing is a function that runs your code and,
on exception, captures the local variables at the failure point.
"""
import sys
import traceback
from typing import Any, Callable


def debug_call(func: Callable, *args: Any, **kwargs: Any) -> dict:
    """Call func(*args, **kwargs) and return a report dict.

    Report shape:
      {"status": "ok",    "result": <return value>}
      {"status": "error", "error_type": "ValueError",
                          "message": str(e),
                          "frame_locals": {...}}

    `frame_locals` is the locals() of the deepest frame inside `func`
    when it raised — that's the "if I'd had a pdb here" snapshot.

    Implementation hints:
      - Wrap the call in try / except Exception as e.
      - Use sys.exc_info() and traceback.extract_tb() OR walk the
        traceback via e.__traceback__ to get the deepest frame.
      - Pull `frame.tb_frame.f_locals` from the deepest tb node.
    """
    # TODO: implement.
    raise NotImplementedError
