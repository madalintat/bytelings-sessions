"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
import typing
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_event_is_typeddict():
    assert typing.is_typeddict(ex.Event)


def test_event_has_required_fields():
    hints = typing.get_type_hints(ex.Event)
    assert "kind" in hints
    assert "user_id" in hints
    assert "amount_cents" in hints
    assert hints["user_id"] is int
    assert hints["amount_cents"] is int


def test_event_kind_is_literal():
    hints = typing.get_type_hints(ex.Event)
    kind_type = hints["kind"]
    assert typing.get_origin(kind_type) is typing.Literal
    assert set(typing.get_args(kind_type)) == {"click", "view", "purchase"}


def test_revenue_empty():
    assert ex.revenue([]) == 0


def test_revenue_basic():
    events = [
        {"kind": "click", "user_id": 1, "amount_cents": 0},
        {"kind": "purchase", "user_id": 1, "amount_cents": 1000},
        {"kind": "view", "user_id": 2, "amount_cents": 0},
        {"kind": "purchase", "user_id": 3, "amount_cents": 500},
    ]
    assert ex.revenue(events) == 1500


def test_revenue_no_purchases():
    events = [
        {"kind": "click", "user_id": 1, "amount_cents": 999},
        {"kind": "view", "user_id": 2, "amount_cents": 0},
    ]
    # 999 was on a click — not counted.
    assert ex.revenue(events) == 0
