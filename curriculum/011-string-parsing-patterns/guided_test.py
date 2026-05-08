"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_full_line():
    out = ex.parse_contact("Smith;John;John@Acme.com;+1 (415) 555-1212")
    assert out == {
        "name": "John Smith",
        "email": "john@acme.com",
        "phone": "14155551212",
    }


def test_apostrophe_in_last():
    out = ex.parse_contact("O'Hara;Aoife;aoife@x.io;")
    assert out == {"name": "Aoife O'Hara", "email": "aoife@x.io", "phone": ""}


def test_only_one_field():
    out = ex.parse_contact("Solo")
    assert out == {"name": "Solo", "email": "", "phone": ""}


def test_extra_whitespace():
    out = ex.parse_contact("  Smith ; John ; john@x.io ; 415.555.0144 ")
    assert out["name"] == "John Smith"
    assert out["email"] == "john@x.io"
    assert out["phone"] == "4155550144"


def test_empty_line():
    out = ex.parse_contact("")
    assert out == {"name": "", "email": "", "phone": ""}


def test_only_first_blank():
    out = ex.parse_contact("Smith;;john@x.io;5551212")
    assert out["name"] == "Smith"
