"""Rung 3: Guided — solved version.

`time.perf_counter()` gives sub-millisecond precision. The `try/finally`
block ensures we record elapsed time even if the body raises — we
capture the end time before any exception handling happens.
"""
import time
from contextlib import contextmanager


@contextmanager
def timing(label: str, sink: list):
    t0 = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - t0
        sink.append((label, elapsed))
