---
day: 060-custom-exceptions-eafp-vs-lbyl
phase: phase-3-quality-production
module: module-11-errors-eafp-debugging
style: compare
---
# Day 60 — EAFP vs LBYL, and why you'll write your own exceptions

You're writing a billing service. A user submits a charge. You need
to check the customer exists and has a valid payment method. Two
styles, both common, very different feel.

## Side by side

**LBYL — Look Before You Leap.** Check first, then act:

```python
def charge(customer_id: str, cents: int) -> None:
    if customer_id not in db.customers:
        return
    customer = db.customers[customer_id]
    if customer.payment_method is None:
        return
    if not customer.payment_method.is_valid():
        return
    customer.payment_method.charge(cents)
```

**EAFP — Easier to Ask Forgiveness than Permission.** Try, then handle:

```python
def charge(customer_id: str, cents: int) -> None:
    try:
        db.customers[customer_id].payment_method.charge(cents)
    except KeyError:
        raise CustomerNotFound(customer_id)
    except AttributeError:
        raise NoPaymentMethod(customer_id)
    except InvalidPaymentMethod:
        raise  # already a domain error, let it bubble
```

Pick: which would you rather debug at 2 AM?

The EAFP version has one happy-path line. The LBYL version has four
guards that will silently drift out of sync with reality (what if a
new field gets added to `payment_method`? The guard misses it).

Pythonic Python prefers EAFP **when the failure is exceptional**
(file vanished, key absent, network blew up). LBYL is right when
checking is *cheap and the failure is normal flow* (e.g., `if not
items: return`).

## Why custom exceptions earn their keep

Built-in exceptions are about *Python*: `KeyError`, `ValueError`,
`OSError`. Your business has its *own* failure modes: a customer
without a payment method, a charge under the minimum, a refund past
the window. Wrap those in a domain exception:

```python
class BillingError(Exception):
    """Base for all billing-domain failures."""

class CustomerNotFound(BillingError): ...
class NoPaymentMethod(BillingError): ...
class InvalidPaymentMethod(BillingError): ...
```

Three wins:

1. **Callers can catch your domain.** `except BillingError` catches
   the family without listing every leaf.
2. **Tracebacks read like English.** "InvalidPaymentMethod at
   billing.py:42" beats "AttributeError: 'NoneType' object has no
   attribute 'charge'".
3. **You can attach context.** Override `__init__` to take
   `customer_id`, `amount`, etc. They show up in logs for free.

The hierarchy mirrors the built-in tree: a single root, narrow leaves,
catch the narrowest you can handle.

## Now: open `fluency.py`

A function written in heavy LBYL style. Rewrite it EAFP.
