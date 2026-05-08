"""Rung 2: Fluency drill — fix the bug AND lock it in.

Topic: systematic debugging — never ship a fix without a regression test.

`apply_discount` should subtract `discount_cents` from `price_cents`,
clamped at zero (a discount can't make the price negative). It has a
bug: when the discount is bigger than the price, it returns a negative
number.

Step 1: read the bug above.
Step 2: fix `apply_discount`.
Step 3: open the test file and add ONE more test that would have
        caught this bug. The placeholder there names what to add.
"""


def apply_discount(price_cents: int, discount_cents: int) -> int:
    # TODO: clamp at zero. Currently returns negative on big discount.
    return price_cents - discount_cents
