"""Rung 5 tests — write these yourself using pytest's monkeypatch fixture.

The function under test (`is_production_env`) is in apply.py. It
reads `os.environ["APP_ENV"]` and returns one of three values.

Your job: cover all three branches WITHOUT touching the real
environment. Use `monkeypatch.setenv("APP_ENV", "<value>")` to set,
and `monkeypatch.delenv("APP_ENV", raising=False)` to remove.

These tests are STARTERS — they all currently fail with
NotImplementedError. Replace the bodies. The `_byte.diagnose` helper
gives you targeted teaching messages on common wrong answers.

Run:
    uv run pytest apply_test.py -v
"""
import importlib.util
from pathlib import Path

import pytest

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_5"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "apply.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_returns_production_when_env_is_production(monkeypatch: pytest.MonkeyPatch):
    # TODO: monkeypatch.setenv APP_ENV=production, then call
    # ex.is_production_env() and check it returns "production".
    raise NotImplementedError


def test_returns_staging_when_env_is_staging(monkeypatch: pytest.MonkeyPatch):
    # TODO: monkeypatch APP_ENV=staging, assert "staging".
    raise NotImplementedError


def test_returns_unknown_when_env_is_unset(monkeypatch: pytest.MonkeyPatch):
    # TODO: monkeypatch.delenv APP_ENV (raising=False so the test passes
    # even if APP_ENV happened to not be set in the real environment).
    # Then assert "unknown".
    raise NotImplementedError


# ----- below: the diagnostic-flavored versions of the same tests, but
# already filled in. They show the diagnose pattern in action. The
# learner doesn't have to write these — they're the "correct" reference,
# kept here to demonstrate the helper. -----


def test_production_with_diagnose(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("APP_ENV", "production")
    actual = ex.is_production_env()
    diagnose(
        actual == "production",
        f"Expected 'production', got {actual!r} for APP_ENV=production.",
        (lambda: actual == "unknown",
         "Returned 'unknown' even though APP_ENV is 'production'. "
         "Did the function read APP_ENV at import time instead of "
         "in the function body? It must read lazily — monkeypatch "
         "sets the env AFTER the import."),
    )


def test_unknown_when_unset_with_diagnose(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv("APP_ENV", raising=False)
    actual = ex.is_production_env()
    diagnose(
        actual == "unknown",
        f"Expected 'unknown' when APP_ENV unset, got {actual!r}.",
        (lambda: actual == "",
         "Returned the empty string instead of 'unknown'. The "
         "function must coerce missing/empty/unrecognized to 'unknown' "
         "explicitly."),
    )
