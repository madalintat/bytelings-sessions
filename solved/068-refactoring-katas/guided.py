"""Rung 3: Guided implement — solved version.

Replace the if/elif chain with a dict lookup. COSTS maps country to
cost; shipping_cost delegates to .get() with the international fallback.
The "DE"/"FR"/"IT"/"ES" group is populated by iteration.
"""

COSTS: dict[str, int] = {
    "US": 5,
    "CA": 7,
    "MX": 10,
    "UK": 12,
    **{c: 15 for c in ("DE", "FR", "IT", "ES")},
}


def shipping_cost(country: str) -> int:
    """Return shipping cost for `country`, or the international flat rate."""
    return COSTS.get(country, 25)
