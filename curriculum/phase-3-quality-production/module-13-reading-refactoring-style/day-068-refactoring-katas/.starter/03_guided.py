"""Rung 3: Guided implement — replace conditional with a lookup table.

Topic: the "replace conditional with table" refactor.

The `shipping_cost` below is a long if/elif chain. Refactor it to use
a module-level dict + one .get() lookup, plus the international flat
rate fallback.

Behavior contract (must not change):
  - "US"      -> 5
  - "CA"      -> 7
  - "MX"      -> 10
  - "UK"      -> 12
  - "DE"/"FR"/"IT"/"ES" -> 15
  - anything else        -> 25

Approach:
  1. Define module-level COSTS: dict[str, int] mapping country -> cost.
     (You may collapse "DE"/"FR"/"IT"/"ES" by listing each, or use a
     loop to populate the dict — your call.)
  2. Implement `shipping_cost(country) -> int` as a single .get() with
     the 25 default.
"""


# TODO: define COSTS as a dict.
COSTS: dict[str, int] = {}


def shipping_cost(country: str) -> int:
    """Return shipping cost for `country`, or the international flat rate."""
    # TODO: one-liner with COSTS.get(country, 25)
    if country == "US":
        return 5
    elif country == "CA":
        return 7
    elif country == "MX":
        return 10
    elif country == "UK":
        return 12
    elif country in ("DE", "FR", "IT", "ES"):
        return 15
    else:
        return 25
