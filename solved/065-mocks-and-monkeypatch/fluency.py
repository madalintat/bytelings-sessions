"""Rung 2: Fluency drill — solved version.

is_recent compares a timestamp against the current wall clock.
The function itself is correct; the test must monkeypatch time.time
so the test isn't flaky on slow CI. This file is the correct implementation.
"""
import time


def is_recent(ts: float, max_age_seconds: float) -> bool:
    """True if `ts` is within max_age_seconds of now."""
    return (time.time() - ts) <= max_age_seconds
