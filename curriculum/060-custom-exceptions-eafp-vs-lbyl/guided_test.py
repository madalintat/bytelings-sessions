"""Tests for rung 3."""
import importlib.util
from pathlib import Path

import pytest

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "03_guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_customer_not_found_subclass():
    assert issubclass(ex.CustomerNotFound, ex.BillingError)


def test_no_payment_method_subclass():
    assert issubclass(ex.NoPaymentMethod, ex.BillingError)


def test_customer_not_found_message():
    err = ex.CustomerNotFound("c99")
    assert err.customer_id == "c99"
    assert "c99" in str(err)


def test_no_payment_method_message():
    err = ex.NoPaymentMethod("c1")
    assert err.customer_id == "c1"
    assert "c1" in str(err)


def test_charge_success():
    customers = {"c1": {"payment_method": "visa-1234"}}
    assert ex.charge(customers, "c1", 500) == 500


def test_charge_missing_customer():
    with pytest.raises(ex.CustomerNotFound) as info:
        ex.charge({}, "c99", 500)
    assert info.value.customer_id == "c99"


def test_charge_no_payment_method():
    customers = {"c2": {"payment_method": None}}
    with pytest.raises(ex.NoPaymentMethod) as info:
        ex.charge(customers, "c2", 500)
    assert info.value.customer_id == "c2"


def test_billing_error_catches_both():
    """The whole point of a base class — one except catches the family."""
    customers = {}
    try:
        ex.charge(customers, "c99", 500)
    except ex.BillingError:
        pass
    else:
        pytest.fail("expected BillingError")
