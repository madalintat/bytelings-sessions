"""Tests for rung 3 — example tests + a property round-trip."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)

try:
    from hypothesis import given, strategies as st

    HAS_HYPOTHESIS = True
except ImportError:
    HAS_HYPOTHESIS = False


def test_alnum_passes_through():
    assert ex.encode("Hello123") == "Hello123"


def test_space_encoded():
    assert ex.encode("a b") == "a%20b"


def test_decode_reverses_space():
    assert ex.decode("a%20b") == "a b"


def test_unicode_encoded():
    s = "café"
    encoded = ex.encode(s)
    assert "é" not in encoded
    assert ex.decode(encoded) == s


@pytest.mark.skipif(not HAS_HYPOTHESIS, reason="hypothesis not installed")
def test_round_trip_property():
    @given(st.text())
    def _check(s):
        assert ex.decode(ex.encode(s)) == s

    _check()


@pytest.mark.skipif(not HAS_HYPOTHESIS, reason="hypothesis not installed")
def test_encoded_is_ascii():
    """Encoded output must be pure ASCII alphanumeric + '%'."""
    @given(st.text())
    def _check(s):
        out = ex.encode(s)
        for ch in out:
            assert ch.isascii() and (ch.isalnum() or ch == "%"), out

    _check()
