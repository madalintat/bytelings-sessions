"""Rung 3: Guided implement.

Topic: a timing context manager

Implement `timing(label, sink)` as a @contextmanager:
- On entry, record the time (use time.perf_counter()).
- On exit, append (label, elapsed_seconds) to `sink`.

Use try/finally so the timing record is added even if the body raises.

>>> events = []
>>> with timing("work", events):
...     pass
>>> events[0][0]
'work'
"""
import time
from contextlib import contextmanager


# TODO: add @contextmanager
def timing(label: str, sink: list):
    # TODO: t0 = time.perf_counter(); try: yield; finally: append result
    raise NotImplementedError
