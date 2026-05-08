"""Rung 4: Solo implement.

Topic: a real refactor with a hidden bug.

Below is a single tangled function. The hidden tests pin its INTENDED
behavior — which is NOT the same as its current behavior. Your job:

  1. Refactor `analyze_orders` so the behavior matches the docstring.
  2. The function takes a list of order dicts and returns a summary
     dict. The CURRENT code mishandles refunded orders (it counts
     them in revenue). That's the bug. Find it during refactoring,
     not before.

Public API: `analyze_orders(orders) -> dict` with these keys:
  - "count":          number of NON-REFUNDED orders
  - "refunded_count": number of refunded orders
  - "revenue":        sum of `total` for non-refunded orders
  - "refunded_amount": sum of `total` for refunded orders

Hidden tests in 04_solo_test.py. Your refactored code should also
have NO function longer than 15 lines (a soft style check).
"""


def analyze_orders(orders: list[dict]) -> dict:
    count = 0
    refunded_count = 0
    revenue = 0
    refunded_amount = 0
    for order in orders:
        # BUG: this branch increments revenue for refunded orders too.
        if order.get("refunded", False):
            refunded_count += 1
            refunded_amount += order["total"]
            revenue += order["total"]
        else:
            count += 1
            revenue += order["total"]
    return {
        "count": count,
        "refunded_count": refunded_count,
        "revenue": revenue,
        "refunded_amount": refunded_amount,
    }
