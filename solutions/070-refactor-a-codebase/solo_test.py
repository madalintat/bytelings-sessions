"""HIDDEN tests for rung 4 — behavior tests + style check."""
import importlib.util
import inspect
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_no_orders():
    assert ex.analyze_orders([]) == {
        "count": 0,
        "refunded_count": 0,
        "revenue": 0,
        "refunded_amount": 0,
    }


def test_one_normal_order():
    assert ex.analyze_orders([{"total": 50}]) == {
        "count": 1,
        "refunded_count": 0,
        "revenue": 50,
        "refunded_amount": 0,
    }


def test_one_refunded_order_does_not_count_in_revenue():
    """The bug. Revenue must NOT include refunded amounts."""
    assert ex.analyze_orders([{"total": 50, "refunded": True}]) == {
        "count": 0,
        "refunded_count": 1,
        "revenue": 0,
        "refunded_amount": 50,
    }


def test_mixed():
    orders = [
        {"total": 100},
        {"total": 50, "refunded": True},
        {"total": 25},
        {"total": 75, "refunded": True},
    ]
    assert ex.analyze_orders(orders) == {
        "count": 2,
        "refunded_count": 2,
        "revenue": 125,
        "refunded_amount": 125,
    }


def test_function_under_limit():
    """Soft style check: refactored function body should be short."""
    src = inspect.getsource(ex.analyze_orders)
    body_lines = [ln for ln in src.splitlines()[1:] if ln.strip()]
    assert len(body_lines) <= 15, (
        f"analyze_orders is too long ({len(body_lines)} lines) — "
        "extract a helper"
    )
