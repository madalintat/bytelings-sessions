"""Tests for rung 2."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "02_fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_renamed():
    assert hasattr(ex, "normalize_email_inplace"), (
        "rename `validate_email` to `normalize_email_inplace`"
    )


def test_old_name_gone():
    assert not hasattr(ex, "validate_email"), (
        "remove the old `validate_email` name once renamed"
    )


def test_behavior_unchanged():
    fn = getattr(ex, "normalize_email_inplace", None)
    if fn is None:
        return  # the test above already failed loud
    record = {"email": "  ADA@LoVeLaCe.org "}
    out = fn(record)
    assert out["email"] == "ada@lovelace.org"
    assert out is record  # in-place — same object
