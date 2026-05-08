"""Rung 3: Guided — solved version.

Sort by finish time (not start). The exchange argument shows that swapping
any other first choice for the earliest-finishing activity never makes things
worse — and potentially frees up more room for later activities.

Key: back-to-back is allowed (start >= last_finish, not strict >).
"""


def select_activities(activities: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Return the maximum-size subset of non-overlapping activities."""
    # Sort by finish time — the canonical greedy key.
    sorted_acts = sorted(activities, key=lambda a: a[1])
    chosen: list[tuple[int, int]] = []
    last_finish = float("-inf")
    for start, finish in sorted_acts:
        if start >= last_finish:
            chosen.append((start, finish))
            last_finish = finish
    return chosen
