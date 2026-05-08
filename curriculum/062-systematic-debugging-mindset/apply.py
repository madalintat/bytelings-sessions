"""Rung 5: Apply.

Demo: a faulty processor that crashes on a specific batch of orders.
We use `minimize` from rung 4 to shrink the failing batch to the
smallest contiguous slice that still triggers the bug — exactly what
you'd do in a real outage post-mortem.

Try it: uv run python apply.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

_spec = spec_from_file_location("_solo", Path(__file__).parent / "solo.py")
_solo = module_from_spec(_spec)
_spec.loader.exec_module(_solo)


def crashes_on(orders: list[dict]) -> bool:
    """Simulated bug: processor crashes if it sees an order with
    quantity=0 followed by an order with currency='XBT'."""
    for i in range(len(orders) - 1):
        if orders[i].get("qty") == 0 and orders[i + 1].get("ccy") == "XBT":
            return True
    return False


FAILING_BATCH = [
    {"id": 1, "qty": 3, "ccy": "USD"},
    {"id": 2, "qty": 5, "ccy": "EUR"},
    {"id": 3, "qty": 1, "ccy": "USD"},
    {"id": 4, "qty": 0, "ccy": "USD"},   # the trigger pair
    {"id": 5, "qty": 7, "ccy": "XBT"},   # the trigger pair
    {"id": 6, "qty": 2, "ccy": "USD"},
    {"id": 7, "qty": 9, "ccy": "EUR"},
]


def main() -> None:
    print(f"failing batch size: {len(FAILING_BATCH)}")
    minimal = _solo.minimize(FAILING_BATCH, crashes_on)
    print(f"minimal repro size: {len(minimal)}")
    for o in minimal:
        print(f"  {o}")


if __name__ == "__main__":
    main()
