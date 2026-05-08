"""Rung 3: Guided implement.

Topic: filtering + transforming with one comprehension

You're given a list of (user_id, score) tuples. Return the set of
user_ids whose score is at least `threshold`. Use a single set
comprehension.
"""


def passing_users(scores: list[tuple[int, int]], threshold: int) -> set[int]:
    """Return the set of user ids whose score >= threshold.

    >>> sorted(passing_users([(1, 90), (2, 50), (3, 80)], 70))
    [1, 3]
    >>> passing_users([], 50)
    set()
    """
    # TODO: one set comprehension. Pattern: {expr for x in iterable if cond}
    raise NotImplementedError
