"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_basic():
    e = ex.Email("test@example.com")
    assert e.address == "test@example.com"


def test_strips_whitespace():
    e = ex.Email("  test@example.com  ")
    assert e.address == "test@example.com"


def test_lowercases():
    e = ex.Email("Test@Example.COM")
    assert e.address == "test@example.com"


def test_empty_raises():
    with pytest.raises(ValueError):
        ex.Email("")


def test_whitespace_only_raises():
    with pytest.raises(ValueError):
        ex.Email("   ")


def test_no_at_raises():
    with pytest.raises(ValueError):
        ex.Email("noatsign.com")


def test_two_ats_raises():
    with pytest.raises(ValueError):
        ex.Email("a@b@c.com")


def test_repr():
    e = ex.Email("test@example.com")
    assert repr(e) == "Email('test@example.com')"


def test_domain():
    e = ex.Email("Test@Example.COM")
    assert e.domain() == "example.com"
