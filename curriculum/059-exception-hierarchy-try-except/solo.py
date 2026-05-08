"""Rung 4: Solo implement.

Topic: routing different exception types to different recovery paths.

Implement `classify_failure(callable_, *args)` that:
  - Calls `callable_(*args)` and returns ("ok", result) on success.
  - On `LookupError` (KeyError, IndexError) returns ("missing", None).
  - On `ValueError` returns ("bad_value", None).
  - On `OSError` (FileNotFoundError, PermissionError, ...) returns ("io", None).
  - Lets any other exception propagate (do NOT catch Exception).

Hidden tests in 04_solo_test.py.

Patterns: P-05 (eafp-try-then-fallback).
"""
from typing import Any, Callable


def classify_failure(callable_: Callable, *args: Any) -> tuple[str, Any]:
    raise NotImplementedError
