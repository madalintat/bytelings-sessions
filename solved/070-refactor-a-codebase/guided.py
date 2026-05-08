"""Rung 3: Guided implement — solved version.

Extract mean_of(records, field) to deduplicate the three averaging
helpers. Fix the avg_speed bug (empty list returned 1.0, now 0.0).
"""


def mean_of(records: list[dict], field: str) -> float:
    """Return the average of `field` across `records`. Empty -> 0.0."""
    if not records:
        return 0.0
    return sum(r[field] for r in records) / len(records)


def avg_score(records: list[dict]) -> float:
    return mean_of(records, "score")


def avg_age(records: list[dict]) -> float:
    return mean_of(records, "age")


def avg_speed(records: list[dict]) -> float:
    return mean_of(records, "speed")
