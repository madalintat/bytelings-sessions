"""Rung 2: Fluency drill — fix the flaky test using monkeypatch.

Topic: replacing `time.time` so a time-sensitive test is deterministic.

`is_recent(ts, max_age_seconds)` returns True if `ts` is within the
last `max_age_seconds` seconds, using the current wall clock.

The function is fine. The TEST is the problem — it computes
"recent" using the real clock, so on a slow CI machine the test
might race the freshness window and flake. Edit 02_fluency_test.py
and use monkeypatch to freeze `time.time`.
"""
import time


def is_recent(ts: float, max_age_seconds: float) -> bool:
    """True if `ts` is within max_age_seconds of now."""
    return (time.time() - ts) <= max_age_seconds
