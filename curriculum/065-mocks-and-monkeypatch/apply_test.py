"""Rung 5 tests — monkeypatch in action.

Three plain tests for `is_production_env` (in apply.py) cover the
three branches of os.environ["APP_ENV"]: production, staging, unset.
Each uses pytest's `monkeypatch` fixture to set or unset APP_ENV
without touching the real environment, so tests stay isolated.

The two `*_with_diagnose` tests below show the same scenarios with
the `_byte.diagnose` helper layered on top — when the assertion fails,
the learner gets a teaching message instead of a generic string diff.

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
    monkeypatch.setenv("APP_ENV", "production")
    assert ex.is_production_env() == "production"


def test_returns_staging_when_env_is_staging(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("APP_ENV", "staging")
    assert ex.is_production_env() == "staging"


def test_returns_unknown_when_env_is_unset(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv("APP_ENV", raising=False)
    assert ex.is_production_env() == "unknown"


# ----- below: the same three scenarios but with the `diagnose` helper
# wrapped around each. Compare the two styles to see what diagnose
# adds: targeted teaching messages on common wrong answers. -----


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
