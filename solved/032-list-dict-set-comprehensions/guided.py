"""Rung 3: Guided — solved version.

A set comprehension collapses both the filter (`if score >= threshold`)
and the transformation (keep only `user_id`) into one expression. Because
the output is a set, duplicate user_ids are automatically deduplicated —
there is no need for an explicit uniqueness check.
"""


def passing_users(scores: list[tuple[int, int]], threshold: int) -> set[int]:
    """Return the set of user ids whose score >= threshold.

    >>> sorted(passing_users([(1, 90), (2, 50), (3, 80)], 70))
    [1, 3]
    >>> passing_users([], 50)
    set()
    """
    return {user_id for user_id, score in scores if score >= threshold}
