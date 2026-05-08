"""Rung 3: Guided implement — a small custom-exception hierarchy.

Topic: defining domain exceptions and using them with EAFP.

Real-world framing: a tiny billing module. You'll define three
exception classes and one function that uses them.
"""


class BillingError(Exception):
    """Base for all billing-domain failures."""


# TODO: define CustomerNotFound(BillingError) that takes a customer_id
# in __init__ and stores it on `self.customer_id`. Its str() should
# read: f"customer not found: {customer_id}".
class CustomerNotFound(BillingError):
    def __init__(self, customer_id: str) -> None:
        # TODO: store customer_id on self and call super().__init__(...)
        raise NotImplementedError


# TODO: define NoPaymentMethod(BillingError) — same shape as above
# but the message reads: f"no payment method for customer: {customer_id}".
class NoPaymentMethod(BillingError):
    def __init__(self, customer_id: str) -> None:
        raise NotImplementedError


def charge(customers: dict, customer_id: str, cents: int) -> int:
    """Charge `cents` to `customer_id`'s payment method.

    `customers` is a dict like:
        {"c1": {"payment_method": "visa-1234"}, "c2": {"payment_method": None}}

    Returns the cents charged on success.
    Raises CustomerNotFound if the customer isn't in the dict.
    Raises NoPaymentMethod if `payment_method` is None.

    Implementation: write it in EAFP style (try / except KeyError, etc.).
    """
    # TODO: implement EAFP style. Catch KeyError -> CustomerNotFound.
    # Then check payment_method; raise NoPaymentMethod if None.
    raise NotImplementedError
