"""Rung 4: Solo implement.

Topic: build a function whose tests will use monkeypatch.

Implement `current_user_greeting() -> str`:

  - Reads env var `USER_NAME`.
  - If set and non-empty, returns f"Hello, {name}!".
  - If unset OR empty, returns "Hello, stranger!".

Reads from `os.environ`. The hidden tests use monkeypatch.setenv /
delenv — so your function must read env LAZILY (each call), not once
at import time.

Patterns: P-05 (eafp-try-then-fallback), P-07 (accumulator-into-dict), P-19 (context-manager-protocol).
"""
import os


def current_user_greeting() -> str:
    raise NotImplementedError
