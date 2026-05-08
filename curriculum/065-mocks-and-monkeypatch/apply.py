"""Rung 5: Apply — write tests for env-var-driven code using monkeypatch.

Solo (rung 4) had you write a function that reads env vars; the
hidden tests already used monkeypatch on it. The lesson there was
"write code that's testable." This rung flips it: the function is
provided; YOUR job is to write the test.

Below is `is_production_env()`. It reads `os.environ["APP_ENV"]` and
returns one of three categorical answers. There are three branches —
production / staging / unknown — and you need to cover all three
without your test ever touching the real environment of the machine
running pytest.

Open `apply_test.py` next to this file. It imports `is_production_env`
from here. Fill in the three test bodies using pytest's `monkeypatch`
fixture (`monkeypatch.setenv`, `monkeypatch.delenv`).

Concept (the day's NEW one): monkeypatch is for testing YOUR
env-aware code in isolation. It mutates `os.environ` for the test's
lifetime and restores it on teardown — so a test that sets
APP_ENV=production cannot leak into the next test. That's the
property that makes env-driven code testable at all.

Self-check:
    uv run pytest apply_test.py

Patterns: P-05 (eafp-try-then-fallback), P-07 (accumulator-into-dict), P-19 (context-manager-protocol).
"""
from __future__ import annotations

import os


def is_production_env() -> str:
    """Return one of {"production", "staging", "unknown"}.

    - APP_ENV=="production"  → "production"
    - APP_ENV=="staging"     → "staging"
    - APP_ENV unset, empty,
      or any other value     → "unknown"

    Reads env LAZILY (each call), not once at import time, so
    monkeypatch can change it under the function's feet.
    """
    value = os.environ.get("APP_ENV", "").strip()
    if value == "production":
        return "production"
    if value == "staging":
        return "staging"
    return "unknown"
