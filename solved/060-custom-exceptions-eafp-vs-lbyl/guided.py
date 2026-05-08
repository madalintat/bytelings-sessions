"""Rung 3: Guided — solved version.

`CustomerNotFound` and `NoPaymentMethod` both inherit from
`BillingError`, which itself inherits from `Exception`. Callers can
catch the base `BillingError` for all billing errors, or the specific
subclasses for fine-grained handling.

`charge` is written EAFP: we attempt `customers[customer_id]` and let
the `KeyError` guide us to `CustomerNotFound` rather than checking
`if customer_id in customers` first.
"""


class BillingError(Exception):
    """Base for all billing-domain failures."""


class CustomerNotFound(BillingError):
    def __init__(self, customer_id: str) -> None:
        self.customer_id = customer_id
        super().__init__(f"customer not found: {customer_id}")


class NoPaymentMethod(BillingError):
    def __init__(self, customer_id: str) -> None:
        self.customer_id = customer_id
        super().__init__(f"no payment method for customer: {customer_id}")


def charge(customers: dict, customer_id: str, cents: int) -> int:
    """Charge `cents` to `customer_id`'s payment method."""
    try:
        record = customers[customer_id]
    except KeyError:
        raise CustomerNotFound(customer_id)
    if record.get("payment_method") is None:
        raise NoPaymentMethod(customer_id)
    return cents
