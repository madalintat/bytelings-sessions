"""Rung 3: Guided implement — deduplicate three near-identical helpers.

Topic: extract the common shape; the difference often IS the bug.

Below are three helpers that compute the average of a numeric field
across a list of records. They're nearly identical — but one of them
has a subtle bug. Your task:

  1. Extract one helper `mean_of(records, field)` that does the
     common work correctly.
  2. Rewrite `avg_score`, `avg_age`, and `avg_speed` to delegate
     to `mean_of`.
  3. Keep the public function names — callers depend on them.

The bug-finder is the test: once dedup'd, all three pass the same
correctness test, including the empty-list case.
"""


def avg_score(records: list[dict]) -> float:
    if len(records) == 0:
        return 0.0
    total = 0
    for r in records:
        total += r["score"]
    return total / len(records)


def avg_age(records: list[dict]) -> float:
    if len(records) == 0:
        return 0.0
    total = 0
    for r in records:
        total += r["age"]
    return total / len(records)


def avg_speed(records: list[dict]) -> float:
    # BUG: this branch returns 1.0 for empty input. Spot it after dedup.
    if len(records) == 0:
        return 1.0
    total = 0
    for r in records:
        total += r["speed"]
    return total / len(records)


# TODO: extract `mean_of(records, field) -> float` and have all three
# delegate to it. Make sure empty input -> 0.0 in all three.
