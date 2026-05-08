"""Rung 4: Solo implement — solved version.

The bug: refunded orders were also added to `revenue`. The refactor
makes it clear by removing the incorrect `revenue += order["total"]`
from the refunded branch. Two small helpers keep each function under
15 lines.
"""


def _is_refunded(order: dict) -> bool:
    return bool(order.get("refunded", False))


def analyze_orders(orders: list[dict]) -> dict:
    """Summarize orders, separating refunded from non-refunded revenue."""
    count = refunded_count = revenue = refunded_amount = 0
    for order in orders:
        if _is_refunded(order):
            refunded_count += 1
            refunded_amount += order["total"]
        else:
            count += 1
            revenue += order["total"]
    return {"count": count, "refunded_count": refunded_count,
            "revenue": revenue, "refunded_amount": refunded_amount}
