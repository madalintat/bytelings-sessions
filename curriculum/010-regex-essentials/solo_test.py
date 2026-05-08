"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty():
    assert ex.find_emails("") == []


def test_no_emails():
    assert ex.find_emails("just some plain text, no @ here") == []


def test_basic():
    assert ex.find_emails("hi alice@example.com bye") == ["alice@example.com"]


def test_multiple():
    assert ex.find_emails("a@b.co and c@d.io") == ["a@b.co", "c@d.io"]


def test_lowercased():
    assert ex.find_emails("Foo@Bar.COM") == ["foo@bar.com"]


def test_subdomains():
    assert ex.find_emails("ping ops@mail.acme.example.org now") == [
        "ops@mail.acme.example.org"
    ]


def test_plus_and_dots_in_local():
    assert ex.find_emails("alice.smith+filter@example.com") == [
        "alice.smith+filter@example.com"
    ]


def test_short_tld_excluded():
    # Single-letter TLD is rejected by the spec
    assert ex.find_emails("x@y.z") == []
