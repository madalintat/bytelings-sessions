"""HIDDEN tests for rung 4 — do not peek before solving 04_solo.py."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "04_solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def make_catalog():
    return {
        "111": {"title": "Calculus", "borrower": None},
        "222": {"title": "SICP", "borrower": "alice"},
    }


def test_hierarchy():
    assert issubclass(ex.BookNotFound, ex.LibraryError)
    assert issubclass(ex.AlreadyCheckedOut, ex.LibraryError)


def test_book_not_found_attrs():
    err = ex.BookNotFound("999")
    assert err.isbn == "999"
    assert "999" in str(err)


def test_already_checked_out_attrs():
    err = ex.AlreadyCheckedOut("222", "alice")
    assert err.isbn == "222"
    assert err.borrower == "alice"
    assert "222" in str(err)


def test_checkout_success():
    catalog = make_catalog()
    rec = ex.checkout(catalog, "111", "bob")
    assert rec["borrower"] == "bob"
    assert catalog["111"]["borrower"] == "bob"


def test_checkout_missing():
    with pytest.raises(ex.BookNotFound):
        ex.checkout(make_catalog(), "999", "bob")


def test_checkout_already_out():
    with pytest.raises(ex.AlreadyCheckedOut) as info:
        ex.checkout(make_catalog(), "222", "bob")
    assert info.value.borrower == "alice"


def test_caught_via_base():
    try:
        ex.checkout(make_catalog(), "999", "bob")
    except ex.LibraryError:
        pass
    else:
        pytest.fail("expected LibraryError")
