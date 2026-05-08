"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_with_user(monkeypatch):
    monkeypatch.setenv("USER_NAME", "ada")
    assert ex.current_user_greeting() == "Hello, ada!"


def test_with_empty_user(monkeypatch):
    monkeypatch.setenv("USER_NAME", "")
    assert ex.current_user_greeting() == "Hello, stranger!"


def test_without_user(monkeypatch):
    monkeypatch.delenv("USER_NAME", raising=False)
    assert ex.current_user_greeting() == "Hello, stranger!"


def test_isolation(monkeypatch):
    """Setting in one test must not leak into the next."""
    monkeypatch.delenv("USER_NAME", raising=False)
    assert ex.current_user_greeting() == "Hello, stranger!"
